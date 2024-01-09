class Solution:
    def checkZeroOnes(self, s: str) -> bool:
      count_zeros = 1 - int(s[0])
      count_ones = int(s[0])
      max_zeros = count_zeros
      max_ones = count_ones
      
      for i in range(1, len(s)):
        if s[i] != s[i - 1]:
          max_zeros = max(max_zeros, count_zeros)
          max_ones = max(max_ones, count_ones)
          count_zeros = count_ones = 0
        
        count_zeros += 1 - int(s[i])
        count_ones += int(s[i])
      
      max_zeros = max(max_zeros, count_zeros)
      max_ones = max(max_ones, count_ones)
      return max_ones > max_zeros
        