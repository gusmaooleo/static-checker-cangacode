'''
Coordenará o fluxo de execução do analizador léxico (syntax-driven).
'''
from syntax.initializer import Initializer
from syntax.normalizer import Normalizer
from lexer.token import Token
from lexer.lexer import Lexer

class Controller:
  def __init__(self, path: str) -> None:
    self.path = path

  def run(self):
    source = Initializer().read_source(self.path)
    formatted_source = self.applyFilters(source)
    lex, tab = self.lexer(formatted_source)
    print("------------------------------------------")
    print("")
    print("")
    print("Tokens (.LEX)")
    for i in lex:
      print("-------------------------------------------------------------------------------------------------------------")
      print(i)

    
  
  def applyFilters(self, source: list[str]) -> list[str]:
    '''
    Versão do arquivo em lista é enviado para o pipe de normalização e adequação
    para leitura do normalizador.
    Returns:
      str: Versão do arquivo pronta para ser lida pelo reconhecedor.
    '''
    normalizer = Normalizer(source)
    return normalizer.pipe()
  
  def lexer(self, lines: list[str]) -> tuple[list[Token], dict[str, dict]]:
    '''
    Roda o lexer, lendo o arquivo e dividindo atriubições e keywords em tokens.
    '''
    lex: list[Token] = []
    lexer = Lexer(lines)

    while True:
      token = lexer.run()
      if token.code == "EOF":
        break
      lex.append(token)

    print("------------------------------------------")
    print("")
    print("")
    print("Tabela de símbolos (.TAB)")
    keys = lexer.symbol_table.keys()
    for i in keys:
      print("-------------------------------------------------------------------------------------------------------------")
      print(lexer.symbol_table[i])

    
    return lex, lexer.symbol_table
  
  def afdeterministic(self):
    '''
    Implementa a rotina do reconhecedor.
    '''
    return
