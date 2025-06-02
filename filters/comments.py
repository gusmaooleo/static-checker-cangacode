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

# window = False

# for i in range(len(source)):
#   if source[i].startswith("/*"):
#     window = True
#     source[i] = "\n"
#   elif source[i].startswith("*/") and window:
#     window = False
#     source[i] = "\n"
#   else:
#     for j in range(1, len(source[i])):
#       if source[i][j - 1] + source[i][j] == "//":
#         source[i] = source[i][:j - 1].strip() + "\n"
#         break
#       elif source[i][j - 1] + source[i][j] == "/*":
#         # print(source[i], 'slice de ', j + 1, 'ate', source[i].find("*/"), source[i][j + 1 : source[i].find("*/")])
#         source[i] = source[i][:j - 1].strip() + source[i][source[i].find("*/") + 2:].strip()  + "\n"
#         print(source[i])
#         print(len(source[i]))
#         break

#   if window:
#     source[i] = "\n"
#
