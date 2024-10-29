class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        dp = [[0] * 2 for _ in range(M)]

        for i in range(M):
            dp[i][0] = 1

        max_moves = 0

        for j in range(1, N):
            for i in range(M):
                if grid[i][j] > grid[i][j - 1] and dp[i][0] > 0:
                    dp[i][1] = max(dp[i][1], dp[i][0] + 1)

                if (
                    i - 1 >= 0
                    and grid[i][j] > grid[i - 1][j - 1]
                    and dp[i - 1][0] > 0
                ):
                    dp[i][1] = max(dp[i][1], dp[i - 1][0] + 1)

                if (
                    i + 1 < M
                    and grid[i][j] > grid[i + 1][j - 1]
                    and dp[i + 1][0] > 0
                ):
                    dp[i][1] = max(dp[i][1], dp[i + 1][0] + 1)

                max_moves = max(max_moves, dp[i][1] - 1)

            for k in range(M):
                dp[k][0] = dp[k][1]
                dp[k][1] = 0

        return max_moves 