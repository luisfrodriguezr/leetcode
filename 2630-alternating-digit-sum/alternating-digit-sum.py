import math
class Solution:
  def alternateDigitSum(self, n: int) -> int:
    ans = 0
    sign = 1 if int(math.log10(n)) % 2 == 0 else -1

    while n:
      ans += sign * (n % 10)
      n //= 10
      sign *= -1
    
    return ans