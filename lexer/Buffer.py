'''
Abstrai o avanço na leitura, pular espaços, 
contar linhas, etc.
'''

class Buffer:
  def __init__(self, lines: list[str]) -> None:
    self.lines = lines
    self.line_no = 0
    self.col_no = 0

  def peek(self) -> str:
    '''Olha o caractere atual sem consumir.'''
    if self.eof():
      return ""
    return self.lines[self.line_no][self.col_no]

  def advance(self) -> str:
    '''
    Consome e retorna o caractere atual.
    Atualiza linha/coluna automaticamente ao encontrar '\n' ou fim de linha.
    '''
    if self.eof():
      return ""
    ch = self.lines[self.line_no][self.col_no]
    self.col_no += 1
    if self.col_no >= len(self.lines[self.line_no]):
      self.line_no += 1
      self.col_no = 0
    return ch

  def eof(self) -> bool:
    '''Retorna True se chegamos ao fim de todas as linhas.'''
    return self.line_no >= len(self.lines)

  def skip_whitespace(self):
    '''Pula espaços, tabs e quebras de linha, mantendo contagem correta de linhas.'''
    while not self.eof() and self.peek() in {" ", "\t", "\n", "\r"}:
      self.advance()
