class Solution:
  def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
    ans = 0
    hs1 = set()
    hs2 = set()

    for num in arr1:
      s = str(num)
      prefix = ''
      for c in s:
        prefix += c
        hs1.add(prefix)
    
    for num in arr2:
      s = str(num)
      prefix = ''
      for c in s:
        prefix += c
        hs2.add(prefix)
    
    for k in hs1: ans = max(ans, len(k) * (k in hs2))

    return ans



        