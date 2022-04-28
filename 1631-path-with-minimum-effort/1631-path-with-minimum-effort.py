class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        grid = heights
        # edge cases:
        if not grid:
            return 0
        
        from heapq import heappush, heappop
        h = [(0, (0,0))] # key to heap is cost
        costSoFar = {(0,0): 0} # also serves as a more nuanced visited set
        # cameFrom = {(0,0): None} # (child : parent) Only required for path finding (not needed in scope)
        dirs = [(1,0), (0,1), (-1,0), (0,-1)] # all 4 dirs
        trgt = (len(grid)-1, len(grid[0])-1) # Dijkstra can have early termination condition
        import math
        while h:
            cost, node = heappop(h)
            x, y = node
            if node == trgt: # - Dikstra can have early terminate
                break
            for dir in dirs:
                newX, newY = x+dir[0], y+dir[1]
                # boundries
                if newX >= 0 and newX <= len(grid)-1 and newY >= 0 and newY <= len(grid[0])-1:
                    edgeCost = max(cost, abs(grid[x][y] - grid[newX][newY])) # -- See [Comment I] below
                    # if nei not seen before or seen before but now revisiting via less costly route
                    if (newX, newY) not in costSoFar or ( (newX, newY) in costSoFar and edgeCost < costSoFar[(newX, newY)]):
                        costSoFar[(newX, newY)] = edgeCost
                        heappush(h, (edgeCost, (newX, newY)))
                        
        return costSoFar[trgt]