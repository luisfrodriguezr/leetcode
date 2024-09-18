class Solution:
  def minMaxDifference(self, num: int) -> int:
    mi = list()
    ma = list()
    d = -1
    n = str(num)

    for c in n:
      a = c
      if c == '9' or c == d: 
        a = '9'
      elif d == -1:
        d = c
        a = '9'

      ma.append(a)

    d = n[0]
    for c in n:
      a = c
      if c == d:
        a = '0'
      mi.append(a)
  
    return int(''.join(ma)) - int(''.join(mi))
        