class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      memo = [[-1 for _ in text2] for _ in text1]
      def LCS(p1, p2):
        if p1 == len(text1) or p2 == len(text2):
          return 0
        if memo[p1][p2] >= 0:
          return memo[p1][p2]
        
        problem_1 = LCS(p1 + 1, p2)
        
        problem_2 = 0
        np2 = text2.find(text1[p1], p2)
        if np2 != -1:
          problem_2 = 1 + LCS(p1 + 1, np2 + 1)
        
        memo[p1][p2] = max(memo[p1][p2], max(problem_1, problem_2))
        return memo[p1][p2]
      
      return LCS(0, 0)
      
       
      
      
        
      
      
      
        