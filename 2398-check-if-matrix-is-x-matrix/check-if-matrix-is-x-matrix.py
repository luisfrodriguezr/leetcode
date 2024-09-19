class Solution:
  def checkXMatrix(self, grid: List[List[int]]) -> bool:
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if ((i == j or (i + j) == (len(grid) - 1)) and grid[i][j] == 0) or ((i != j and (i + j) != (len(grid)) - 1) and grid[i][j] != 0):
          return False
    
    return True
        