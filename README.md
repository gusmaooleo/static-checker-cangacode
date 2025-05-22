- [x] **1. Leitura do Arquivo .251 e Pré-Processamento**
  - [x] Passo 1.1: Ler o arquivo `.251` e normalizar todo o texto para maiúsculas.  
  - [x] Passo 1.2: Remover comentários (`/* ... */` e `// ...`) e filtrar caracteres inválidos, mantendo apenas espaços, tabs, `\n`, `\r` e os caracteres da linguagem (letras, dígitos, símbolos, operadores, aspas).

- [ ] **2. Análise Léxica (Iterativa e com Gestão de Estado)**
  - [ ] Passo 2.1: Inicializar um cursor de posição (`pos = 0`) e a tabela de símbolos vazia.  
  - [ ] Passo 2.2: Para cada chamada ao analisador léxico:
    - [ ] Ignorar espaços em branco repetidos até o próximo caractere significativo.  
    - [ ] Ler caracteres válidos até encontrar um delimitador ou atingir 32 caracteres de lexeme.  
    - [ ] Truncar o lexeme a 32 caracteres, mas continuar consumindo até o delimitador.  
    - [ ] Filtrar caracteres inválidos durante a leitura do lexeme (por exemplo, `VAR#1` → `VAR1`).  
    - [ ] Classificar o átomo (identificador, número, operador, etc.) e retornar:  
      - Código do átomo (ex.: `IDN02`).  
      - Índice na tabela de símbolos (se aplicável).  
      - Nova posição (`pos`) após o token.  
    - [ ] Atualizar a tabela de símbolos com lexeme truncado, tipo (a inferir) e linhas de ocorrência.

- [ ] **3. Controle de Escopo e Tipagem**
  - [ ] Passo 3.1: Manter uma pilha de escopos para rastrear blocos (`FUNCTION`, `IF`, `WHILE`, etc.).  
  - [ ] Passo 3.2: Inferir tipos de identificadores durante a análise:
    - [ ] Atribuição direta (`ID := 10`) → tipo `IN`.  
    - [ ] Uso em string (`"texto"`) → tipo `ST`.  

- [ ] **4. Validação por Autômatos (Simplificada)**
  - [ ] Passo 4.1: Implementar autômatos mínimos para regras-chave (ex.: declaração de variáveis `VAR ID := VALOR ;` → `SUB01`).  
  - [ ] Passo 4.2: Validar a sequência de tokens conforme esses autômatos, sem análise sintática completa.

- [ ] **5. Geração dos Relatórios**
  - [ ] Passo 5.1: Gerar o relatório `.LEX` com a lista de tokens na ordem de ocorrência, incluindo lexeme, código, índice na tabela e número da linha.  
  - [ ] Passo 5.2: Gerar o relatório `.TAB` com a tabela de símbolos, exibindo entrada, código, lexeme truncado, tipo e linhas de ocorrência.

- [ ] **Aspectos Críticos Adicionais**
  - [ ] Bufferização de entrada: opcional, usar buffer de duas metades para arquivos grandes.  
  - [ ] Truncamento coerente: garantir que o corte em 32 caracteres não quebre o token (ex.: não cortar aspas no meio).  
  - [ ] Erros silenciosos: caracteres inválidos devem ser ignorados sem gerar erro.  
  - [ ] Contagem de linhas: preservar quebras de linha mesmo dentro de comentários para manter numeração correta.  
