class Solution:
  def tupleSameProduct(self, nums: List[int]) -> int:
    hash_map = dict()
    ans = 0
    
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        prod = nums[i] * nums[j]
        hash_map[prod] = hash_map.get(prod, -1) + 1
        if hash_map[prod] > 0:
          ans += hash_map[prod]
    
    return ans * 8;
      