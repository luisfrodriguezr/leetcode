class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    hash_table = [-1] * (2 ** 8)
    left = ans = 0
    
    for right in range(len(s)):
      hash_key = ord(s[right])
      
      if hash_table[hash_key] >= left:
        left = hash_table[hash_key] + 1
      
      ans = max(ans, right - left + 1)
      hash_table[hash_key] = right
      
    return ans
      
        