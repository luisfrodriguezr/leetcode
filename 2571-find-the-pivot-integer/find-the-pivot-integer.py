class Solution:
  def pivotInteger(self, n: int) -> int:
    x = math.sqrt(n * (n + 1) / 2)

    if int(x) == x: return int(x)

    return -1
        