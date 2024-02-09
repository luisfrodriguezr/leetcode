class Solution:
  def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    nums.sort()
    ans = list()
    dp = [1] * len(nums)
    hash_map = dict()
    last = ma = 0
    
    def find(n):
      if n == hash_map[n]:
        ans.append(n)
        return 
      find(hash_map[n])
      ans.append(n)
      return 
      
    for i, num in enumerate(nums):
      hash_map[num] = num
      for j in range(0, i):
        if num % nums[j] == 0:
          if dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            hash_map[num] = nums[j]
      if dp[i] > ma:
        ma = dp[i]
        last = num
    
    find(last)
    
    return ans