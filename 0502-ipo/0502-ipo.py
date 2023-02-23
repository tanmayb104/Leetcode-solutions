class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()
        i = 0
        maximizeCapital = []
        while k > 0:
            while i < n and projects[i][0] <= w:
                heapq.heappush(maximizeCapital, -projects[i][1])
                i += 1
            if not maximizeCapital:
                break
            w -= heapq.heappop(maximizeCapital)
            k -= 1
        return w