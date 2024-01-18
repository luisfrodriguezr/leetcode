class Solution:
    def climbStairs(self, n: int) -> int:
      ans = [1, 2, 3]
      for i in range(3, n):
        ans.append(ans[i - 1] + ans[i - 2])
      
      return ans[n - 1]
      
        