'''
Lexer: responsável por ler caracteres e gerar tokens 
com tipo e lexema.
'''

from lexer.Buffer import Buffer
from lexer.token import Token
from lexer.states import State
from lexer.lexer_tokens import identifier_tokens, reserved_symbols, symbols_ops

class Lexer:
  def __init__(self, lines: list[str]) -> None:
    self.buf = Buffer(lines)
    self.symbol_table: dict[str, dict] = {}
    self.single_char_symbols = { k for k in symbols_ops.keys() if len(k) == 1 }
    self.symbol_scope: str = State.VARIABLE.name

  def run(self) -> Token:
    self.buf.skip_whitespace()
    if self.buf.eof():
      return Token(lexeme="", code="EOF", sym_index=None, line=self.buf.line_no)
    
    start_line = self.buf.line_no
    ch = self.buf.peek()

    if ch.isalpha() or ch == '_':
      lex, rawLex = self.read_while(lambda c: c.isalnum() or c == '_')
      self.setScope(lex)
      code = reserved_symbols.get(lex, identifier_tokens[self.symbol_scope])
      sym_index = None
      if code == identifier_tokens[self.symbol_scope]:
        is_array = (self.buf.peek() == '[')
        type_code = self._infer_type(code, is_array=is_array)
        sym_index = self.add_identifier(lex, code, start_line, raw_length=len(rawLex), type_code=type_code)
        
      return Token(lex, code, sym_index, start_line)

    if ch.isdigit():
      lex = self.read_number()
      code = identifier_tokens["REALCONST"] if "." in lex else identifier_tokens["INTCONST"] 
      return Token(lex, code, None, start_line)
    
    if ch == '"':
      lex = self.read_string_literal()
      return Token(lex, identifier_tokens["STRINGCONST"], None, start_line)
    
    if ch == "'":
      lex = self.read_char_literal()
      return Token(lex, identifier_tokens["CHARCONST"], None, start_line)
    
    two = self.buf.peek(2)
    if two in symbols_ops:
      self.buf.advance(); self.buf.advance()
      return Token(two, symbols_ops[two], None, start_line)
    if ch in symbols_ops:
      self.buf.advance()
      return Token(ch, symbols_ops[ch], None, start_line)
    
    '''Falta implementação de sub-máquinas dinâmicas. (será feita após implementação dos automatos)'''

    if ch in self.single_char_symbols:
      self.buf.advance()
      return Token(ch, symbols_ops[ch], None, start_line)

    self.buf.advance()
    return self.run()
    
  def read_while(self, cond):
    result = ""
    rawResult = ""
    while not self.buf.eof() and cond(self.buf.peek()):
      result += self.buf.advance()
      if len(result) >= 32:
        rawResult = result
        while not self.buf.eof() and cond(self.buf.peek()):
          rawResult += self.buf.advance()
        break
    return result, rawResult

  def read_number(self) -> str:
    """
    Lê um número inteiro ou real (com parte decimal e opcionalmente exponencial).
    Retorna o lexeme completo (até 32 chars, se truncamento for aplicado).
    """
    lexeme = ""
    raw_count = 0
    has_dot = False

    while not self.buf.eof():
      ch = self.buf.peek()
      if ch.isdigit():
        raw_count += 1
        if len(lexeme) < 32:
          lexeme += self.buf.advance()
        else:
          self.buf.advance()
      elif ch == "." and not has_dot:
        if len(lexeme) == 31:
          break
        has_dot = True
        raw_count += 1
        if len(lexeme) < 32:
          lexeme += self.buf.advance()
        else:
          self.buf.advance()
      else:
        break

    if not self.buf.eof() and self.buf.peek().lower() == "e":
      if len(lexeme) >= 32:
        return lexeme

      raw_count += 1
      lexeme += self.buf.advance()

      if self.buf.peek() in {"+", "-"}:
        if len(lexeme) < 32:
          raw_count += 1
          lexeme += self.buf.advance()
        else:
          self.buf.advance()

      while not self.buf.eof() and self.buf.peek().isdigit():
        raw_count += 1
        if len(lexeme) < 32:
          lexeme += self.buf.advance()
        else:
          self.buf.advance()

    return lexeme


  def read_string_literal(self):
    out = self.buf.advance()
    while not self.buf.eof() and self.buf.peek() != '"':
      out += self.buf.advance()
    out += self.buf.advance()
    
    if len(out) > 32:
        return out[:34] + '"' 
    return out

  def read_char_literal(self):
    out = self.buf.advance()
    out += self.buf.advance()
    out += self.buf.advance()
    return out
  
  def add_identifier(self, lexeme: str, code: str, line: int, raw_length: int, type_code: str):
    """
    Insere/atualiza symbol_table e retorna o índice (1-based)
    da entry correspondente.
    """
    symbol_name = lexeme + code

    if symbol_name not in self.symbol_table:
      self.symbol_table[symbol_name] = {
        "lexeme": lexeme,
        "code": code,
        "raw_length": raw_length,
        "trunc_length": len(lexeme),
        "type_code": type_code,
        "lines": [line],
      }
    else:
      entry = self.symbol_table[symbol_name]
      if line not in entry["lines"] and len(entry["lines"]) < 5:
        entry["lines"].append(line)
    
    idx = list(self.symbol_table.keys()).index(symbol_name) + 1
    self.symbol_scope = State.VARIABLE.name
    return idx
  
  def _infer_type(self, code: str, is_array: bool = False) -> str:
    """
    Retorna a sigla de tipo (2 letras) para o identificador:
    - escalares: VD, IN, FP, ST, CH, BL, …
    - arrays  : AF, AI, AS, AC, AB
    """
    scalar_map = {
      "IDN01": "VD",  # programName
      "IDN02": "IN",  # variable padrão
      "IDN03": "VD",  # functionName
      "IDN04": "IN",  # intConst
      "IDN05": "FP",  # realConst
      "IDN06": "ST",  # stringConst
      "IDN07": "CH",  # charConst
    }
    
    array_map = {
      "IDN02": "AI",  # variável de inteiro em vetor
      "IDN04": "AI",  # intConst em vetor
      "IDN05": "AF",  # realConst em vetor
      "IDN06": "AS",  # stringConst em vetor
      "IDN07": "AC",  # charConst em vetor
    }

    if is_array:
      return array_map.get(code, "")
    else:
      return scalar_map.get(code, "")

  
  def setScope(self, lex=""):
    if "_" in lex:
      self.symbol_scope = State.VARIABLE.name
      return
    
    match lex:
      case State.FUNCTIONNAME.value:
        self.symbol_scope = State.FUNCTIONNAME.name
        return
      case State.PROGRAMNAME.value:
        self.symbol_scope = State.PROGRAMNAME.name
        return
    