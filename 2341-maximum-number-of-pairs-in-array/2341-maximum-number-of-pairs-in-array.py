class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
      hashTable = dict()
      pairs = left = 0
      for num in nums:
        hashTable[num] = hashTable.get(num, 0) + 1
        if hashTable[num] == 2:
          pairs += 1
          hashTable[num] = 0
      
      for num in hashTable:
        if hashTable[num]: left += 1
      
      return [pairs, left]
        