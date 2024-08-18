class Solution:
  def findFinalValue(self, nums: List[int], original: int) -> int:
    hs = set()

    for num in nums:
      hs.add(num)
    
    while original in hs:
      original *= 2

    return original
        