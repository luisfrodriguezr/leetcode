class Solution:
  def findErrorNums(self, nums: List[int]) -> List[int]:
    hash_map = dict()
    ans = [0, 0]
    
    for i in range(1, len(nums) + 1):
      hash_map[i] = 0
      
    for num in nums:
      hash_map[num] += 1
      
    for num in hash_map:
      if hash_map[num] == 2:
        ans[0] = num
      if hash_map[num] == 0:
        ans[1] = num
        
    return ans