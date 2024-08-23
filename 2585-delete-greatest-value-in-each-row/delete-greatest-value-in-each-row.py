class Solution:
  def deleteGreatestValue(self, grid: List[List[int]]) -> int:
    ans = 0

    for i in range(len(grid)):
      grid[i].sort()

    for i in range(len(grid[0])):
      m = 0
      for j in range(len(grid)):
        m = max(m, grid[j][i])
      ans += m
    
    return ans
        