'''
Lexer: responsável por ler caracteres e gerar tokens 
com tipo e lexema.
'''

from lexer.Buffer import Buffer
from lexer.token import Token
from lexer.lexer_tokens import identifier_tokens, reserved_symbols

class Lexer:
  def __init__(self, lines: list[str]) -> None:
    self.buf = Buffer(lines)
    self.symbol_table: dict[str, dict] = {}

  def run(self) -> Token:
    self.buf.skip_whitespace()
    if self.buf.eof():
      return Token(lexeme="", code="EOF", sym_index=None, line=self.buf.line_no)
    
    start_line = self.buf.line_no
    ch = self.buf.peek()

    if ch.isalpha() or ch == '_':
      lex = self.read_while(lambda c: c.isalnum() or c == '_')
      code = reserved_symbols.get(lex, identifier_tokens["variable"])
      sym_index = None
      if code == identifier_tokens["variable"]:
          sym_index = self.add_identifier(lex, code, start_line, raw_length=len(lex))
      return Token(lex, code, sym_index, start_line)
    
    return
  
  def read_while(self, cond):
    result = ""
    while not self.buf.eof() and cond(self.buf.peek()):
      result += self.buf.advance()
      if len(result) >= 32:
        while not self.buf.eof() and cond(self.buf.peek()):
          self.buf.advance()
        break
    return result

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
        has_dot = True
        raw_count += 1
        if len(lexeme) < 32:
          lexeme += self.buf.advance()
        else:
          self.buf.advance()
      else:
        break

    if not self.buf.eof() and self.buf.peek().lower() == "e":
      raw_count += 1
      if len(lexeme) < 32:
        lexeme += self.buf.advance()
      else:
        self.buf.advance()

      if self.buf.peek() in {"+", "-"}:
        raw_count += 1
        if len(lexeme) < 32:
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
    return out

  def read_char_literal(self):
    out = self.buf.advance()
    out += self.buf.advance()
    out += self.buf.advance()
    return out
  
  def add_identifier(self, name: str, line: int, col: int):
    """
    Se o nome não estiver na tabela, cria uma entry.
    Retorna o dict da entry.
    """
    if name not in self.symbol_table:
      self.symbol_table[name] = {
          "token": identifier_tokens["variable"],
          "lexeme": name,
          "line": line,
          "col": col,
      }
    return self.symbol_table[name]
  