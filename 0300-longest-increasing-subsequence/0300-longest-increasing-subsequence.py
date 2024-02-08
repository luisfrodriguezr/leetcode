class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    dp = [1] * len(nums)
    ans = 0
    for i, num in enumerate(nums):
      
      for j in range(0, i):
        if nums[j] < num:
          dp[i] = max(dp[i], dp[j] + 1)
      
      ans = max(ans, dp[i])

    return ans
