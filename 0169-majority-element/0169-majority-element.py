class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    hash_map = dict()
    ans = None
    m = 0
    
    for num in nums:
      hash_map[num] = hash_map.get(num, 0) + 1
      if hash_map[num] > m:
        ans = num
        m = hash_map[num]
    
    return ans
        