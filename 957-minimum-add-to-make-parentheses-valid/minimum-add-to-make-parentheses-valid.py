class Solution:
  def minAddToMakeValid(self, s: str) -> int:
    stack = list()

    for c in s:
      if c == ')':
        if len(stack) == 0:
          stack.append(c)
        elif stack[-1] == '(':
          stack.pop()
        else:
          stack.append(c)
      else:
        stack.append('(')
    
    return len(stack)

        