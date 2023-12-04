class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
      ans = []
      for i in range(1, 101):
        count = 0
        count += 1 if i in nums1 else 0
        count += 1 if i in nums2 else 0
        count += 1 if i in nums3 else 0
        if count >= 2:
          ans.append(i)
      return ans
        