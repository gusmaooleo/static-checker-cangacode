'''
Será responsável por gerar os relatórios finais a partir 
dos dados obtidos da análise léxica (.lex e .tab).
'''
from lexer.token import Token

def generateReports(lex: list[Token], tab: dict[str, dict], filename: str):
  export_lex(lex, filename)
  export_tab(tab, filename)


def export_lex(lex: list[Token], filename: str):
  with open(f'{filename}.lex', "w", encoding="utf-8") as f:
    f.write(
"""Código da Equipe: EQ02
Componentes:
  Bryan Montgomery Hamilton; bryan.hamilton@ucsal.edu.br; 71 99156-4734
  Felipe Gabriel Oliveira da Silva; felipegabriel.silva@ucsal.edu.br; 75 99921-4939
  Leonardo Gabriel Cabral Fernandes Gusmão; leonardo.gusmao@ucsal.edu.br; 71 98397-5022
  Loren Vitória Cavalcante Santos; loren.santos@ucsal.edu.br; 71 98514-7438
\n""")

    f.write(f"RELATÓRIO DA ANÁLISE LÉXICA. Texto fonte analisado: {filename}.251\n")
    f.write("\n")
    for tok in lex:
      idx = tok.sym_index if tok.sym_index is not None else ""
      raw = tok.lexeme
      line = tok.line

      f.write("-" * 32 + "\n")
      f.write(
f"""Lexeme: {raw},
Código: {tok.code},
ÍndiceTabSimb: {idx},
Linha: {line}\n""")


def export_tab(tab: dict[str, dict], filename: str) -> None:
  with open(f'{filename}.tab', "w", encoding="utf-8") as f:
    f.write(
"""Código da Equipe: EQ02
Componentes:
  Bryan Montgomery Hamilton; bryan.hamilton@ucsal.edu.br; 71 99156-4734
  Felipe Gabriel Oliveira da Silva; felipegabriel.silva@ucsal.edu.br; 75 99921-4939
  Leonardo Gabriel Cabral Fernandes Gusmão; leonardo.gusmao@ucsal.edu.br; 71 98397-5022
  Loren Vitória Cavalcante Santos; loren.santos@ucsal.edu.br; 71 98514-7438
\n""")

    f.write(f"RELATÓRIO DA TABELA DE SÍMBOLOS. Texto fonte analisado: {filename}.251\n")
    f.write("\n")
    for _, entry in tab.items():
      lexeme = entry.get("lexeme", "")
      code = entry.get("code", "")
      raw_length = entry.get("raw_length", "")
      trunc_length = entry.get("trunc_length", "")
      type_code = entry.get("type_code", "")
      lines_list = entry.get("lines", [])
      lines_str = "[" + ", ".join(str(n) for n in lines_list) + "]"

      f.write("-" * 32 + "\n")      
      f.write(
f"""Lexeme: {lexeme},
Código: {code},
QtdCharAntesTrunc: {raw_length},
QtdCharDepoisTrunc: {trunc_length},
TipoSimb: {type_code},
Linhas: {lines_str}\n""")