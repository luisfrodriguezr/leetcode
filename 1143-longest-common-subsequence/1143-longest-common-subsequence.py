class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      memo = [[-1] * len(text2) for _ in text1]

      def LCS(p1, p2):
        if p1 == len(text1) or p2 == len(text2):
            return 0

        if memo[p1][p2] >= 0:
            return memo[p1][p2]

        if text1[p1] == text2[p2]:
            memo[p1][p2] = 1 + LCS(p1 + 1, p2 + 1)
            return memo[p1][p2]

        memo[p1][p2] = max(LCS(p1 + 1, p2), LCS(p1, p2 + 1))
        return memo[p1][p2]

      return LCS(0, 0)
      
       
      
      
        
      
      
      
        