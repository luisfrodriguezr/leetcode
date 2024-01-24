class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
      hash_map = dict()
      
      for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1
      
      ans = -1
      for num in hash_map:
        if hash_map[num] == 1:
          ans = max(ans, num)
      
      return ans
          
        