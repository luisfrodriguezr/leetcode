class Solution:
  def rearrangeArray(self, nums: List[int]) -> List[int]:
    n = len(nums)
    p1 = p2 = 0
    ans = list()
    
    while p1 < n or p2 < n:
      
      if p1 != n:
        while p1 < n:
          if nums[p1] >= 0:
            ans.append(nums[p1])
            p1 += 1
            break
          p1 += 1
      
      if p2 != n:
        while p2 < n:
          if nums[p2] < 0:
            ans.append(nums[p2])
            p2 += 1
            break
          p2 += 1
    
    return ans
        