class Solution:
  def areNumbersAscending(self, s: str) -> bool:
    last = -1
    tmp = ""
    for i, c in enumerate(s):
      if c.isdigit():
        tmp += c 
      if (not c.isdigit() or i + 1 == len(s)) and tmp:
        if int(tmp) > last:
          last = int(tmp)
          tmp = ""
        else:
          return False
    
    return True
        