class Solution:
  def maximumOddBinaryNumber(self, s: str) -> str:
    ones = zeros = 0
    ans = list()
    
    for c in s:
      if c == '1': ones += 1
      else: zeros += 1

    for i in range(ones - 1):
      ans.append("1")
    
    for i in range(zeros):
      ans.append("0")
    
    ans.append("1")
    
    return "".join(ans)
      
        