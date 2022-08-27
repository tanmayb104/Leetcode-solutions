from bisect import bisect_right, insort
from math import inf


class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = -inf
        for l in range(n):
            rowSums = [0] * m
            for r in range(l, n):
                for i in range(m):
                    rowSums[i] += matrix[i][r]
                colSums = [0]
                colSum = 0
                for rowSum in rowSums:
                    colSum += rowSum
                    diff = colSum - k
                    idx = bisect_right(colSums, diff)
                    if idx - 1 >= 0 and colSums[idx - 1] == diff:
                        res = max(res, colSum - colSums[idx - 1])
                        return k
                    elif idx != len(colSums):
                        res = max(res, colSum - colSums[idx])
                    insort(colSums, colSum)
        return res