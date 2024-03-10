class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
      ans = list()
      hash_set = set(nums1)

      for num in nums2:
        if num in hash_set:
          ans.append(num)
          hash_set.remove(num)
      
      return ans
        