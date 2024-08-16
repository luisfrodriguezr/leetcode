class Solution:
  def minimumSum(self, nums: List[int]) -> int:
    ans = 151

    for i in range(len(nums)):
      for j in range(i, len(nums)):
        for k in range(j, len(nums)):
          if nums[i] < nums[j] and nums[k] < nums[j]:
            ans = min(ans, nums[i] + nums[j] + nums[k])
          

    return -1 if ans==151 else ans
            
        