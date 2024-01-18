class Solution:
  def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
    ans = []
    for j in range(len(grid[0])):
      m = 0
      for i in range(len(grid)):
        num = grid[i][j]
        length = 0
        if num:
          length = 1 + int(math.log10(abs(num))) + int(num < 0)
        else:
          length = 1
        m = max(m, length)
      ans.append(m)
    
    return ans
      
        