class Comments:
  def run(self, source: list[str]) -> list[str]:
    """
    Remove todos os comentários de linha (//…) e de bloco (/* … */), inclusive:

    - múltiplos blocos na mesma linha
    - marcadores dentro de strings são ignorados
    - suporta blocos aninhados de /* … */
    """

    result = []
    comment_depth = 0

    for line in source:
      i = 0
      new_line = ""
      in_string = False
      prev_char = None

      while i < len(line):
        c = line[i]
        if comment_depth > 0:
          if c == '/' and i + 1 < len(line) and line[i+1] == '*':
            comment_depth += 1
            i += 2
            continue
          if c == '*' and i + 1 < len(line) and line[i+1] == '/':
            comment_depth -= 1
            i += 2
            continue
          i += 1
          continue
        if in_string:
          if c == '"' and prev_char != '\\':
            in_string = False
          new_line += c
          prev_char = c
          i += 1
          continue
        else:
          if c == '"':
            in_string = True
            new_line += c
            prev_char = c
            i += 1
            continue
          if c == '/' and i + 1 < len(line) and line[i+1] == '/':
            new_line = new_line.rstrip() + "\n"
            break
          if c == '/' and i + 1 < len(line) and line[i+1] == '*':
            comment_depth = 1
            i += 2
            continue
          new_line += c
          prev_char = c
          i += 1
      if comment_depth > 0:
        new_line = "\n"
      else:
        if not new_line.endswith("\n"):
          if new_line.strip() == "":
            new_line = "\n"
          else:
            new_line += "\n"
      result.append(new_line)
    return result