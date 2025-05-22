'''
Símbolos reservados da linguagem CangaCode2025-1.

(identifier_tokens apenas mapeia os símbolos que são 
produtos de atribuições (nomes de funções, variáveis etc.))
'''

reserved_symbols = {
  "integer": "PRS01",
  "real": "PRS02",
  "character": "PRS03",
  "string": "PRS04",
  "boolean": "PRS05",
  "void": "PRS06",
  "true": "PRS07",
  "false": "PRS08",
  "varType": "PRS09",
  "funcType": "PRS10",
  "paramType": "PRS11",
  "declarations": "PRS12",
  "endDeclarations": "PRS13",
  "program": "PRS14",
  "endProgram": "PRS15",
  "functions": "PRS16",
  "endFunctions": "PRS17",
  "endFunction": "PRS18",
  "return": "PRS19",
  "if": "PRS20",
  "else": "PRS21",
  "endIf": "PRS22",
  "while": "PRS23",
  "endWhile": "PRS24",
  "break": "PRS25",
  "print": "PRS26",
}

symbols_ops = {
  ";": "SRS01",
  ",": "SRS02",
  ":": "SRS03",
  ":=": "SRS04",
  "?": "SRS05",
  "(": "SRS06",
  ")": "SRS07",
  "[": "SRS08",
  "]": "SRS09",
  "{": "SRS10",
  "}": "SRS11",
  "+": "SRS12",
  "-": "SRS13",
  "*": "SRS14",
  "/": "SRS15",
  "%": "SRS16",
  "==": "SRS17",
  "!=": "SRS18", # <- (#)
  "#": "SRS18",  # alias para "!="
  "<": "SRS19",
  "<=": "SRS20",
  ">": "SRS21",
  ">=": "SRS22",
}

identifier_tokens = {
  "programName": "IDN01",
  "variable": "IDN02",
  "functionName": "IDN03",
  "intConst": "IDN04",
  "realConst": "IDN05",
  "stringConst": "IDN06",
  "charConst": "IDN07",
}

submachine_tokens: dict[str, str] = {}
