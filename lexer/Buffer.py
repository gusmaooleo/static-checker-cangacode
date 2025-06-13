class Buffer:
  """
  Buffer de duas metades (two-buffer):
  - N = 2048 caracteres por metade
  - cada metade tem um sentinela EOF ('\0') no fim de cada bloco
  - reload automático quando `forward` encontra o sentinela
  - mantém rastreio de números de linha e coluna
  """
  EOF = '\0'
  N = 2048

  def __init__(self, lines: list[str]) -> None:
    # Concatena todas as linhas preservando quebras
    self.input_str = ''.join(lines)
    self.input_len = len(self.input_str)
    self.file_pos = 0

    # Buffer de 2*N + 2 (duas metades + sentinelas)
    self.buffer = [''] * (2 * self.N + 2)
    self.forward = 0

    # Inicializa rastreio de posição
    self.line_no = 1
    self.col_no = 0

    # Carrega ambas as metades
    self._load_half(0)
    self._load_half(1)

  def _load_half(self, half: int) -> None:
    """
    Carrega N caracteres na metade especificada e adiciona sentinela ao final.
    half=0 -> indices [0..N-1], sentinela em N
    half=1 -> indices [N+1..2*N], sentinela em 2*N+1
    """
    start = half * (self.N + 1)
    remaining = self.input_len - self.file_pos
    count = min(self.N, remaining)

    # Copia caracteres reais
    for i in range(count):
      self.buffer[start + i] = self.input_str[self.file_pos]
      self.file_pos += 1

    # Preenche resto com EOF
    for i in range(count, self.N):
      self.buffer[start + i] = self.EOF

    # Marca sentinela
    self.buffer[start + self.N] = self.EOF

  def advance(self) -> str:
    """
    Consome e retorna o próximo caractere.
    Se encontrar sentinela, recarrega a metade e refaz leitura.
    Atualiza forward, line_no e col_no apenas após obter o caractere final.
    """
    # Lê caractere atual
    ch = self.buffer[self.forward]

    # Tratamento de sentinela
    if ch == self.EOF:
      if self.forward == self.N:
        self._load_half(0)
        self.forward = 0
      elif self.forward == 2 * self.N + 1:
        self._load_half(1)
        self.forward = self.N + 1
      else:
        # EOF real
        return ''
      # Após recarga, lê o caractere de fato
      ch = self.buffer[self.forward]

    # Avança ponteiro de leitura
    self.forward += 1

    # Atualiza posição linha/coluna com base no caractere efetivo
    if ch == '\n':
      self.line_no += 1
      self.col_no = 0
    else:
      self.col_no += 1

    return ch

  def peek(self, length: int = 1) -> str:
    """
    Olha adiante sem consumir o buffer.
    Recarrega automaticamente ao encontrar sentinelas.
    """
    result = ''
    pos = self.forward
    for _ in range(length):
      ch = self.buffer[pos]
      if ch == self.EOF:
        if pos == self.N:
          self._load_half(0)
          pos = 0
        elif pos == 2 * self.N + 1:
          self._load_half(1)
          pos = self.N + 1
        else:
          break
        ch = self.buffer[pos]
      result += ch
      pos += 1
    return result

  def eof(self) -> bool:
    """
    Retorna True se não há mais caracteres reais (EOF).
    """
    return (self.file_pos >= self.input_len 
            and self.buffer[self.forward] == self.EOF)

  def skip_whitespace(self) -> None:
    """
    Avança enquanto encontrar espaços, tabs ou quebras de linha.
    """
    while not self.eof() and self.peek() in {' ', '\t', '\n', '\r'}:
      self.advance()
