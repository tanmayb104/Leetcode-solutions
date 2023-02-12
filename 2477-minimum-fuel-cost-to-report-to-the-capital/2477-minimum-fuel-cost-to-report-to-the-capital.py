class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)
        self.ans = 0
        
        def dfs(i, prev, people = 1):
            for x in graph[i]:
                if x == prev: continue
                people += dfs(x, i)
            self.ans += (int(ceil(people / seats)) if i else 0)
            return people
        
        dfs(0, 0)
        return self.ans