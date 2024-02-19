class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0: return False
    return math.pow(2, math.log2(n)) == math.pow(2, int(math.log2(n)))
        