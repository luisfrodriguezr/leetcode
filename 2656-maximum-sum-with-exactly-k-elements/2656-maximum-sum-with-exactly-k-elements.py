class Solution:
  def maximizeSum(self, nums: List[int], k: int) -> int:
    return int((k + max(nums)) * (k - 1 + max(nums)) / 2 - (max(nums) * (max(nums) - 1) / 2))
