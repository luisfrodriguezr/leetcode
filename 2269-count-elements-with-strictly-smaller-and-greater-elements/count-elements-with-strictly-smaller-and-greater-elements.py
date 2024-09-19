class Solution:
    def countElements(self, nums: List[int]) -> int:
      mi = min(nums)
      ma = max(nums)

      return sum(1 if x > mi and x < ma else 0 for x in nums)
        