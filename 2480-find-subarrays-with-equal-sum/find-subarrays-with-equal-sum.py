class Solution:
  def findSubarrays(self, nums: List[int]) -> bool:
    hs = set()

    for i in range(len(nums) - 1):
      su = (nums[i] + nums[i + 1])
      if su in hs: return True
      hs.add(su)
    
    return False
        