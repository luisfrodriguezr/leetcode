class Solution:
  def countSeniors(self, details: List[str]) -> int:
    ans = 0
    
    for detail in details:
      ans += detail[-4: -2] > '60'
    
    return ans
      