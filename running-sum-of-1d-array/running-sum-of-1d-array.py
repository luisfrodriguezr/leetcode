class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      prefix = []
      prefix.append(nums[0])
      for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
      
      return prefix