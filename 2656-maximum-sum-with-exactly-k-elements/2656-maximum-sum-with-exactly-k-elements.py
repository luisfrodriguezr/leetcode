class Solution:
  def maximizeSum(self, nums: List[int], k: int) -> int:
    m = max(nums)
    return int((k + m) * (k - 1 + m) / 2 - (m * (m - 1) / 2))
