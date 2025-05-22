import re

class SpecialCharacters:
  def __init__(self) -> None:
    self.invalid_char_pattern = re.compile(
      r"""[^
        A-Za-z0-9          # letras e dígitos
        \ \t\r\n           # espaço, tab, CR, LF
        _                  # underscore
        ;,\:\[\]\(\)\{\}   # pontuação e delimitadores
        \+\-\*/%           # operadores aritméticos
        <>=!#\?            # operadores relacionais e especiais
        "\"'\.\$           # aspas, ponto e cifrão
      ]""",
      re.VERBOSE
    )

  def run(self, source: list[str]) -> list[str]:
    '''
    Remove caracteres especiais (todos os que não estão 
    presentes na especificação).
    '''
    return [self.invalid_char_pattern.sub("", i) for i in source]
