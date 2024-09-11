class Solution:
  def findMiddleIndex(self, nums: List[int]) -> int:
    su = sum(nums)
    curr = 0

    for i in range(len(nums)):
      if curr == su - curr - nums[i]: return i
      curr += nums[i]

    return -1
        