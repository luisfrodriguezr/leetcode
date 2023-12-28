class Solution:
  def maxVowels(self, s: str, k: int) -> int:
    left = ans = curr = 0

    for right in range(k):
      if s[right] in 'aeiou':
        curr += 1
    ans = curr
    for right in range(k, len(s)):
      if s[right] in 'aeiou':
        curr += 1
      if s[left] in 'aeiou':
        curr -= 1
      ans = max(ans, curr)
      left += 1
      
    return ans 
        
        