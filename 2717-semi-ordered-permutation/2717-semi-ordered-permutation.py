class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
      first = last = 0
      minimum = 51
      maximum = 0
      for i, num in enumerate(nums):
        if num > maximum:
          last = i
          maximum = num
         
        if num < minimum:
          first = i
          minimum = num
          
      return first + len(nums) - 1 - last - (first > last)
        