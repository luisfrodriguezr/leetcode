class Solution:
  def equalPairs(self, grid: List[List[int]]) -> int:
    hash_map = dict()
    ans = 0
    
    for row in grid:
      hash_key = tuple(row)
      hash_map[hash_key] = hash_map.get(hash_key, 0) + 1
    
    for j in range(len(grid[0])):
      row = []
      for i in range(len(grid)):
        row.append(grid[i][j])
      
      ans += hash_map.get(tuple(row), 0)
    
    return ans
        