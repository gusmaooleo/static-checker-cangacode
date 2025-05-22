'''
Entrypoint do static-cheker.
1 - Leitura do arquivo (.251).
2 - Normalização inicial do arquivo para letras maiúsculas.
'''

class Initializer:

  @staticmethod
  def read_source(path: str) -> list[str]:
    '''
    Lê o arquivo de texto preservando as quebras de linha.

    Args:
      path (str): Caminho para o arquivo .251

    Returns:
      list[str]: Cada linha do arquivo é um índice da lista retornada. 
      Caracteres já são retornados em letras maiúsculas.
    '''
    with open(path, "r", encoding="ascii", errors="ignore") as f:
      lines = f.readlines()
    return [line.upper() for line in lines]
  