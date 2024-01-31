class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
      r = c = ans = 0
      for i in range(len(board)):
        for j in range(len(board)):
          if board[i][j] == 'R':
            r, c = i, j
      
      for i in range(r - 1, -1, -1):
        if board[i][c] == 'B':
          break
        if board[i][c] == 'p':
          ans += 1
          break
      for i in range(r + 1, len(board)):
        if board[i][c] == 'B':
          break
        if board[i][c] == 'p':
          ans += 1
          break
      for i in range(c - 1, -1, -1):
        if board[r][i] == 'B':
          break
        if board[r][i] == 'p':
          ans += 1
          break
      for i in range(r + 1, len(board[0])):
        if board[r][i] == 'B':
          break
        if board[r][i] == 'p':
          ans += 1
          break
      
      return ans