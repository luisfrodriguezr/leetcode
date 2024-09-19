class Solution:
  def thousandSeparator(self, n: int) -> str:
    l = list(str(n))
    ans = list()

    for i, c in enumerate(l[::-1]):
      if i % 3 == 0 and i > 0:
        ans.append('.')
      ans.append(c)

    ans.reverse()
    return ''.join(ans)