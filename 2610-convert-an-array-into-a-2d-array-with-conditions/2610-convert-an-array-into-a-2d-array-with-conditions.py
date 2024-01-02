# Time complexity O(n) amortized
# Space complexity O(n)
class Solution:
  def findMatrix(self, nums: List[int]) -> List[List[int]]:
    hashMap = dict()
    ans = []
    # Time cost = n
    for num in nums:
      hashMap[num] = hashMap.get(num, 0) + 1
      
    # Time cost = n amortized
    while len(hashMap):
      row = []
      for key in hashMap:
        if hashMap[key]:
          row.append(key)
          hashMap[key] -= 1
      ans.append(row)
      
      keys = set(hashMap.keys())
      for key in keys:
        if hashMap[key] == 0:
          del hashMap[key]
          
    return ans
    
      