class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    ans = [0] * len(temperatures)
    stack = []
    for i, temp in enumerate(temperatures):
      
      while len(stack):
        if temp <= temperatures[stack[-1]]: break
        n = stack.pop()
        ans[n] = i - n
      
      stack.append(i)
    
    return ans