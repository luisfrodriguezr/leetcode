class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    ans = [0] * len(temperatures)
    stack = []
    for i, temp in enumerate(temperatures):
      
      if len(stack):
        while temp > temperatures[stack[-1]]:
          n = stack.pop()
          ans[n] = i - n
          if len(stack) == 0: break
      
      stack.append(i)
    
    return ans
        