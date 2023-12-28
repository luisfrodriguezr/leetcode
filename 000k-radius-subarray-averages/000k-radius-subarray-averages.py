class Solution:
  def getAverages(self, nums: List[int], k: int) -> List[int]:
    prefix = []
    prefix.append(nums[0])
    for i in range(1, len(nums)):
      prefix.append(nums[i] + prefix[-1])
    
    ans = []
    r = 2*k + 1
    for i in range(len(nums)):
      if i - k < 0 or i + k >= len(nums):
        ans.append(-1)
      else:
        avg = (prefix[i + k] - prefix[i - k] + nums[i - k]) // r
        ans.append(avg)
    
    return ans