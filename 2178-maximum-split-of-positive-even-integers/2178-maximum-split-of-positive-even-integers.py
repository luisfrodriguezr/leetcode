class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
      ans = []
      curr = 0
      i = 2
      
      if finalSum % 2: return [] 
      
      while curr != finalSum:
        curr += i
        if curr > finalSum:
          curr -= ans.pop()
        ans.append(i)
        i += 2
      
      return ans
        