class Solution:
  def numSquares(self, n: int) -> int:
    ans = [n]
    hs = set()

    for i in range(int(sqrt(n)), 0, -1):
      hs.add(i * i)

    for i in range(1, n + 1):
      if i in hs:
        ans.append(1)
        continue

      mi = n
      for k in hs:
        if i - k < 0: continue
        mi = min(mi, ans[i - k] + 1)
      ans.append(mi)

    return ans[n]