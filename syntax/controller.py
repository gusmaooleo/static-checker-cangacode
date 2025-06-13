'''
Coordenará o fluxo de execução do analizador léxico (syntax-driven).
'''
from syntax.initializer import Initializer
from syntax.filter import Filter
from syntax.reports import generateReports
from lexer.token import Token
from lexer.lexer import Lexer

class Controller:
  def __init__(self, path: str, filename: str) -> None:
    self.path = path
    self.filename = filename

  def run(self):
    source = Initializer().read_source(self.path)
    formatted_source = self.applyFilters(source)
    lex, tab = self.lexer(formatted_source)
    generateReports(lex, tab, self.filename)
  
  def applyFilters(self, source: list[str]) -> list[str]:
    '''
    Versão do arquivo em lista é enviado para o pipe de normalização e adequação
    para leitura do normalizador.
    Returns:
      str: Versão do arquivo pronta para ser lida pelo reconhecedor.
    '''
    filter = Filter(source)
    return filter.pipe()
  
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

    return lex, lexer.symbol_table
