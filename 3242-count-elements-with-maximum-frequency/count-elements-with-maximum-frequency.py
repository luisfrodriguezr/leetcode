class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
      hash_map = dict()
      ans = m = 0

      for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1
        m = max(m, hash_map[num])

      for num in hash_map:
        ans += hash_map[num] == m
      
      return ans * m
        
        