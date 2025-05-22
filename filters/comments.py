class Comments:
  def run(self, source: list[str]) -> list[str]:
    '''
    Remove os comentários a partir de 
    linhas iniciadas em '//', '/*' e '*/'.
    '''
    lineComments = [i if not i.startswith("//") else '\n' for i in source]

    window = False
    for i in range(len(lineComments)):
      if lineComments[i].startswith("/*"):
        window = True
        lineComments[i] = "\n"
      elif lineComments[i].startswith("*/") and window:
        window = False
        lineComments[i] = "\n"

      if window:
        lineComments[i] = "\n"

    return lineComments