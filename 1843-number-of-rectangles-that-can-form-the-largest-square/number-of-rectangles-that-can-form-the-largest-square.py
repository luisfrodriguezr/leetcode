class Solution:
  def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
    m = ans = 0

    for rect in rectangles:
      ans += min(rect[0], rect[1]) == m

      if min(rect[0], rect[1]) > m:
        m = min(rect[0], rect[1])
        ans = 1

    return ans