''' 
Receberá o texto fonte previamente lido e irá 
prepara-lo para o reconhecedor.

1 - Remoção de comentários (como // e /****/).
2 - Remoção de caracteres inválidos.
'''
from filters.whitespaces import Whitespaces
from filters.comments import Comments
from filters.specialCharacters import SpecialCharacters

class Filter:
  def __init__(self, source: list[str]) -> None:
    self.source = source

  def pipe(self) -> list[str]:
    '''
    Recebe o texto, e formata:
    1 - Remove espaços extra em branco.
    2 - Remove caracteres especiais (todos que não fazem parte do ASCII).
    3 - Remove comentários.

    Returns:
      list[str]: Versão do arquivo pronta para ser lida pelo reconhecedor.
    '''
    self.removeExtraWhitespaces()
    self.removeComments()
    self.removeSpecialCharacters()
    
    return self.source

  def removeExtraWhitespaces(self):
    self.source = Whitespaces().run(self.source)

  def removeComments(self):
    self.source = Comments().run(self.source)

  def removeSpecialCharacters(self):
    self.source = SpecialCharacters().run(self.source)
