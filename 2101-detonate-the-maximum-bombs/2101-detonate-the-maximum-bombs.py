class Solution:
    def dfs(self, gr, visited, c, i):
        visited[i] = True
        c[0] += 1
        for j in gr[i]:
            if not visited[j]:
                self.dfs(gr, visited, c, j)

    def maximumDetonation(self, bombs):
        n = len(bombs)
        gr = [[] for _ in range(n)]
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i != j:
                    x, y = bombs[j][0], bombs[j][1]
                    distance_sq = (x - x1) ** 2 + (y - y1) ** 2
                    if distance_sq <= r1 ** 2:
                        gr[i].append(j)

        ans = float('-inf')
        for i in range(n):
            c = [0]
            visited = [False] * n
            self.dfs(gr, visited, c, i)
            ans = max(ans, c[0])

        return ans