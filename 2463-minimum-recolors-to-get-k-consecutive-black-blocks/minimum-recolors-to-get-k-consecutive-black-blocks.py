class Solution:
  def minimumRecolors(self, blocks: str, k: int) -> int:
    curr = 0

    for i in range(k):
      curr += blocks[i] == 'B'
    
    m = curr

    for i in range(k, len(blocks)):
      curr -= blocks[i - k] == 'B'
      curr += blocks[i] == 'B'
      m = max(m, curr)

    return k - m
        