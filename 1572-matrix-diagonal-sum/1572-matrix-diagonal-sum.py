class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for row in range(n):
            col = row 
            res += mat[row][col]
        for row in range(n):
            col = n - row - 1
            if row == col: 
                continue
            res += mat[row][col]
        return res