class Solution:
  def countBalls(self, lowLimit: int, highLimit: int) -> int:
    def sum_digits(n):
      ans = 0
      
      while n:
        ans += n % 10
        n //= 10
      
      return ans
    
    hash_map = dict()
    ans = 0
    
    for n in range(lowLimit, highLimit + 1): #inclusive
      s = sum_digits(n)
      hash_map[s] = hash_map.get(s, 0) + 1
      ans = max(ans, hash_map[s])
      
    
    return ans
        