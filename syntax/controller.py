'''
Coordenará o fluxo de execução do analizador léxico (syntax-driven).
'''
from syntax.initializer import Initializer
from syntax.normalizer import Normalizer

class Controller:
  def __init__(self, path: str) -> None:
    self.path = path

  def run(self):
    source = Initializer().read_source(self.path)
    formatted_source = self.applyFilters(source)
    print(''.join(formatted_source))
  
  def applyFilters(self, source: list[str]) -> str:
    '''
    Versão do arquivo em lista é enviado para o pipe de normalização e adequação
    para leitura do normalizador.
    Returns:
      str: Versão do arquivo pronta para ser lida pelo reconhecedor.
    '''
    normalizer = Normalizer(source)
    return normalizer.pipe()
  
  def afdeterministic(self):
    '''
    Implementa a rotina do reconhecedor.
    '''
    return
