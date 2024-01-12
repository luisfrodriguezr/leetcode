class Solution:
    def halvesAreAlike(self, s: str) -> bool:
      left = 0
      right = len(s) - 1
      left_counter = right_counter = 0
      while left < right:
        left_counter += s[left].lower() in ['a', 'e', 'i', 'o', 'u']
        right_counter += s[right].lower() in ['a', 'e', 'i', 'o', 'u']
        left += 1
        right -= 1
        
      return left_counter == right_counter