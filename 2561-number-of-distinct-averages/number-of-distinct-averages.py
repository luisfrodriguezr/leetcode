class Solution:
  def distinctAverages(self, nums: List[int]) -> int:
    hs = set()
    nums.sort()

    for i in range(len(nums) // 2):
      hs.add((nums[i] + nums[len(nums) - i - 1]) / 2)
  
    return len(hs)