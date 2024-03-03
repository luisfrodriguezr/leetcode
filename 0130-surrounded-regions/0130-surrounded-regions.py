class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, i, j):
          if not (0 <= i < n) or not (0 <= j < m): return
          if board[i][j] != "O": return
          board[i][j] = "M" # Mark this cell as saved

          dfs(board, i, j + 1)
          dfs(board, i, j - 1)
          dfs(board, i + 1, j)
          dfs(board, i - 1, j)
      
        m = len(board[0])
        n = len(board)
        for c in range(m):
          dfs(board, 0, c)
        for r in range(n):
          dfs(board, r, m - 1)
        for c in range(m):
          dfs(board, n - 1, c)
        for r in range(n):
          dfs(board, r, 0)
        
        for i in range(n):
          for j in range(m):
            if board[i][j] == "O": board[i][j] = "X"
            elif board[i][j] == "M": board[i][j] = "O"
        
      