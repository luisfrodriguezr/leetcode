class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    hash_set = set()
    left = ans = 0
    
    for right in range(len(s)):
      while s[right] in hash_set:
        hash_set.remove(s[left])
        left += 1
        
      hash_set.add(s[right])
      ans = max(ans, len(hash_set))
    
    return ans
      
        