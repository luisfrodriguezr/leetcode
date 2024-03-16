class Solution:
  def findMaxLength(self, nums: List[int]) -> int:
    hashmap = dict()
    hashmap[0] = -1
    maxlen = count = 0
    
    for i in range(len(nums)):
        count += 1 if nums[i] == 1 else -1
        if count in hashmap:
            maxlen = max(maxlen, i - hashmap[count])
        else:
            hashmap[count] = i
    
    return maxlen 