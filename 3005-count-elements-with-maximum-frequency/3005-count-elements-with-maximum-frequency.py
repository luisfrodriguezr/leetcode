class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
      m = ans = 0
      hashMap = dict()
      for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1
        m = max(m, hashMap[num])
      
      for num in hashMap:
        if hashMap[num] == m:
          ans += hashMap[num]
      
      return ans
      
        
        