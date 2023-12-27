class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
      prefix = []
      ans = 0
      prefix.append(nums[0])
      for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
      
      for i in range(len(nums) - 1):
        if prefix[i] >= (prefix[len(nums) - 1] - prefix[i]):
          ans += 1
      
      return ans