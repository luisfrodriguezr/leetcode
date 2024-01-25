class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    hash_table = [-1] * (2 ** 8)
    left = 0
    ans = 0
    
    for right in range(len(s)):
      key = ord(s[right]) - ord('a')
      
      if hash_table[key] >= 0 and hash_table[key] >= left:
        left = hash_table[key] + 1
      
      ans = max(ans, right - left + 1)
      hash_table[key] = right
      
    return ans
      
        