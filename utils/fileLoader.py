from pathlib import Path
import sys

def fileLoader() -> tuple[str, str]:
  '''
  Arquivos com extensão .251 não existem, portanto o pathlib procura
  por nomenclaturas parciais no diretório e valida aqueles cujo fim é ".251".
  '''
  partial_name = input("Nome do arquivo: ").strip()

  match = next(
    (f for f in Path.cwd().iterdir()
    if f.is_file() and f.stem == partial_name and f.suffix == ".251"),
    None
  )

  if not match:
    print(f"Erro: Arquivo com nome '{partial_name}' e extensão '.251' não encontrado.")
    sys.exit(1)

  return str(match), partial_name