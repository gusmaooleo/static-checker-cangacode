from dataclasses import dataclass

@dataclass
class Token:
  lexeme: str           # o texto original (truncado a 32 chars)
  code: str             # o código do átomo (ex.: "IDN02", "PRS01", "SRS14", "SUB03"…)
  sym_index: int | None # índice na tabela de símbolos (só para identificadores), ou None
  line: int             # número da linha onde o token começou