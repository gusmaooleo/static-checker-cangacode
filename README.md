- [x] **1. Leitura do Arquivo .251 e Pré-Processamento**
  - [x] Passo 1.1: Ler o arquivo `.251` e normalizar todo o texto para maiúsculas.  
  - [x] Passo 1.2: Remover comentários (`/* ... */` e `// ...`) e filtrar caracteres inválidos, mantendo apenas espaços, tabs, `\n`, `\r` e os caracteres da linguagem (letras, dígitos, símbolos, operadores, aspas).

- [x] **2. Análise Léxica (Iterativa e com Gestão de Estado)**
  - [x] Passo 2.1: Inicializar um cursor de posição (`pos = 0`) e a tabela de símbolos vazia.  
  - [x] Passo 2.2: Para cada chamada ao analisador léxico:
    - [x] Ignorar espaços em branco repetidos até o próximo caractere significativo.  
    - [x] Ler caracteres válidos até encontrar um delimitador ou atingir 32 caracteres de lexeme.  
    - [x] Truncar o lexeme a 32 caracteres, mas continuar consumindo até o delimitador.  
    - [x] Filtrar caracteres inválidos durante a leitura do lexeme (por exemplo, `VAR#1` → `VAR1`).  
    - [x] Classificar o átomo (identificador, número, operador, etc.) e retornar:  
      - Código do átomo (ex.: `IDN02`).  
      - Índice na tabela de símbolos (se aplicável).  
      - Nova posição (`pos`) após o token.  
    - [x] Atualizar a tabela de símbolos com lexeme truncado, tipo (a inferir) e linhas de ocorrência.

- [x] **3. Controle de Escopo e Tipagem**
  - [x] Passo 3.1: Manter uma pilha de escopos para rastrear blocos (`FUNCTION`, `IF`, `WHILE`, etc.).  
  - [x] Passo 3.2: Inferir tipos de identificadores durante a análise:
    - [x] Atribuição direta (`ID := 10`) → tipo `IN`.  
    - [x] Uso em string (`"texto"`) → tipo `ST`.  

- [x] **5. Geração dos Relatórios**
  - [x] Passo 5.1: Gerar o relatório `.LEX` com a lista de tokens na ordem de ocorrência, incluindo lexeme, código, índice na tabela e número da linha.  
  - [x] Passo 5.2: Gerar o relatório `.TAB` com a tabela de símbolos, exibindo entrada, código, lexeme truncado, tipo e linhas de ocorrência.

- [ ] **Aspectos Críticos Adicionais**
  - [ ] Bufferização de entrada: opcional, usar buffer de duas metades para arquivos grandes.  
  - [x] Truncamento coerente: garantir que o corte em 32 caracteres não quebre o token (ex.: não cortar aspas no meio).  
  - [x] Erros silenciosos: caracteres inválidos devem ser ignorados sem gerar erro.  
  - [x] Contagem de linhas: preservar quebras de linha mesmo dentro de comentários para manter numeração correta.  
