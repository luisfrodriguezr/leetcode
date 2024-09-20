class Solution:
  def surfaceArea(self, grid: List[List[int]]) -> int:
    ans = 0
    self.g = grid

    for i in range(len(grid)):
      for j in range(len(grid[0])):
        curr = grid[i][j]
        up = self.getHeight(i - 1, j)
        right = self.getHeight(i, j + 1)
        down = self.getHeight(i + 1, j)
        left = self.getHeight(i, j - 1)
        ans += max(0, curr - up) + max(0, curr - right) + max(0, curr - down) + max(0, curr - left)
        ans += (curr > 0) * 2

    return ans
  
  def getHeight(self, i, j):
    n = len(self.g)
    if i < 0 or i >= n or j < 0 or j >= n: return 0
    return self.g[i][j]