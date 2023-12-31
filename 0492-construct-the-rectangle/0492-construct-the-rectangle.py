class Solution:
  def constructRectangle(self, area: int) -> List[int]:
    ans = [0, 0]
    curr = 10000001
    for l in range(1, area + 1):
      if area % l == 0:
        w = area / l
        if w * l == area:
          if abs(w - l) < curr:
            curr = abs(w - l)
            ans[0] = int(max(w, l))
            ans[1] = int(min(w, l))
    return ans