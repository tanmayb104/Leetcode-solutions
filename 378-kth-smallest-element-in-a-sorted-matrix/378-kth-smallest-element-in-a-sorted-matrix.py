import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []

        result = 0
        i = 0
        n = len(matrix)
        visited = [[False]*n for _ in range(n)]
        heapq.heappush(heap, (matrix[0][0], 0, 0))

        while i < k:
            val, row, col = heapq.heappop(heap)
            result = val

            if col + 1 < n and not visited[row][col + 1]:
                heapq.heappush(heap,(matrix[row][col + 1], row, col + 1))
                visited[row][col + 1] = True

            if row + 1 < n and not visited[row + 1][col]:
                heapq.heappush(heap,(matrix[row + 1][col], row + 1, col))
                visited[row + 1][col] = True

            i += 1

        return result