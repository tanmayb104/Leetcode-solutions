class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        noOfRows, noOfCols, res = len(grid), len(grid[0]), 0
        dp = [[-1 for _ in range(noOfCols)] for _ in range(noOfRows)]
        
        def dfs(row: int, col: int, prev: int, dp: List[List[int]], grid: List[List[int]]) -> int:
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] <= prev:
                return 0
            if dp[row][col] != -1: 
                return dp[row][col]
            ans = 1
            for direction in directions:
                newRow, newCol = row + direction[0], col + direction[1]
                ans += dfs(newRow, newCol, grid[row][col], dp, grid)
            dp[row][col] = ans
            return ans
        
        for row in range(noOfRows):
            for col in range(noOfCols):
                res += dfs(row, col, -1, dp, grid)
        return res % (10 ** 9 + 7)