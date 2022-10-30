from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        if m + n - 2 <= k:
            return m + n - 2
        
        manhattan_distance = lambda y, x: m + n - y - x - 2
        neighborhood = lambda y, x: [
            (y, x) for y, x in [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)]
            if 0 <= y < m and 0 <= x < n
        ]
        
        fringe_heap = [(manhattan_distance(0, 0), 0, 0, 0, 0)]
        min_eliminations = defaultdict(lambda: k + 1, {(0, 0): 0})
        
        while fringe_heap:
            estimation, steps, eliminations, y, x = heappop(fringe_heap)
            
            if estimation - steps <= k - eliminations:
                return estimation
            
            for y, x in neighborhood(y, x):
                next_eliminations = eliminations + grid[y][x]

                if next_eliminations < min_eliminations[(y, x)]:
                    heappush(fringe_heap, (steps + 1 + manhattan_distance(y, x), steps + 1, next_eliminations, y, x))
                    min_eliminations[(y, x)] = next_eliminations
        
        return -1