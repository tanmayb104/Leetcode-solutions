class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        visited = set()
        from collections import deque
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: 
                    q.append((i,j))
        if len(q) == len(grid)*len(grid[0]) or len(q) == 0:
            return -1
        
        maxD = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        steps = -1
        while q:
            for i in range(len(q)):
                node = q.popleft()
                x, y = node
                visited.add(node)

                for dir in dirs:
                    newX, newY = x+dir[0], y+dir[1]
                    if newX >= 0 and newX <= len(grid)-1 and \
                        newY >= 0 and newY <= len(grid[0])-1:
                            # not seen:
                            if (newX, newY) not in visited:
                                if grid[newX][newY] == 0: 
                                    q.append((newX, newY))
                                    grid[newX][newY] = 1 
            steps += 1
        return steps