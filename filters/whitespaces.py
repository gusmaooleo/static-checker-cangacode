class Whitespaces:
  def run(self, source: list[str]) -> list[str]:
    '''
    Remove espaços extra em branco, tanto ao fim e início 
    de cada linha, quanto entre átomos (não remove espaços
    extra em branco dentro de áspas, por este ser considerado
    um átomo)

    Returns:
      list[str]: Versão do arquivo original sem espaços extra em branco.
    '''

    for i in range(len(source)):
      source[i] = self.auxRemoveWhitespaces(source[i])
    
    return source
  
  def auxRemoveWhitespaces(self, line: str) -> str:
    '''
    Remove repetições de espaço em branco (colapsa para um só) 
    em todo texto exceto dentro de literais de string ("...").
    Preserva '\n' e mantém tudo dentro das aspas intacto.
    '''
    out = []
    in_str = False
    prev_space = False

    for ch in line:
      if ch == '"':
        out.append(ch)
        in_str = not in_str
        prev_space = False
      elif in_str:
        out.append(ch)
      else:
        if ch == ' ':
          if not prev_space:
            out.append(ch)
          prev_space = True
        else:
          out.append(ch)
          prev_space = False

    return ''.join(out).strip() + "\n"