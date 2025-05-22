class Comments:
  def run(self, source: list[str]) -> list[str]:
    '''
    Remove os comentários a partir de 
    linhas iniciadas em '//', '/*' e '*/'.
    '''
    
    window = False
    for i in range(len(source)):
      if source[i].startswith("/*"):
        window = True
        source[i] = "\n"
      elif source[i].startswith("*/") and window:
        window = False
        source[i] = "\n"
      else:
        for j in range(1, len(source[i])):
          if source[i][j - 1] + source[i][j] == "//":
            source[i] = source[i][:j - 1].strip() + "\n"
            break

      if window:
        source[i] = "\n"
    
    return source