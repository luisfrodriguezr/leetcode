class Solution:
  def thousandSeparator(self, n: int) -> str:
    l = list(str(n))
    ans = list()

    aux = 0

    for i, c in enumerate(l[::-1]):
      if aux % 3 == 0 and aux > 0:
        ans.append('.')
      ans.append(c)
      aux += 1

    ans.reverse()
    return ''.join(ans)