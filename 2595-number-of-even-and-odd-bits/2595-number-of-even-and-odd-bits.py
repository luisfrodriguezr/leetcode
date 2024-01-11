class Solution:
  def evenOddBit(self, n: int) -> List[int]:
    counter = [0, 0]
    i = 0
    while n:
      counter[i % 2] += n % 2
      n = n // 2
      i += 1
    
    return counter
        