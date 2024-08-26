class Solution:
    def minimumSum(self, n: int, k: int) -> int:
      hs = set()
      i = 1
      ans = 0
      l = 0

      while l < n:
        if (k - i) not in hs:
          ans += i
          l += 1
        hs.add(i)
        i += 1
      
      return ans
        
        