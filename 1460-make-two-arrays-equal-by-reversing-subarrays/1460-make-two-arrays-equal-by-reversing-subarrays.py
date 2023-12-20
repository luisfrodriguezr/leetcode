class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
      hashMap = dict()
      for num in target:
        hashMap[num] = hashMap.get(num, 0) + 1
      for num in arr:
        hashMap[num] = hashMap.get(num, 0) - 1
        if hashMap[num] < 0:
          return False
      return True
        