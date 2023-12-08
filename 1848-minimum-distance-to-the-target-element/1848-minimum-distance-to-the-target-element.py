# Time O(n)
# Space O(1)
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
      if nums[start] == target:
        return 0
      i = start - 1
      j = start + 1
      while i >= 0 or j < len(nums):
        if i >= 0:
          if nums[i] == target:
            return abs(start - i)
          i -= 1
        if j < len(nums):
          if nums[j] == target:
            return abs(start - j)
          j += 1
