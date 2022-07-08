class Solution:
    def dp(self, houses, costs, target, house, prevPaint, neighborhood, lookup):
        if house == len(houses):
            return 0 if neighborhood == target else sys.maxsize
        key = (house, prevPaint, neighborhood)
        if key not in lookup:
            if houses[house] == 0:
                cost = sys.maxsize
                for j in range(len(costs[house])):
                    currentPaint = j+1
                    cost = min(cost, costs[house][j] + self.dp(houses, costs, target, house+1, currentPaint, neighborhood+int(currentPaint != prevPaint), lookup))
                lookup[key] = cost
            else:
                lookup[key] = self.dp(houses, costs, target, house+1, houses[house], neighborhood+int(houses[house] != prevPaint), lookup)
        return lookup[key]
    
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        cost = self.dp(houses, cost, target, 0, 0, 0, {})
        return cost if cost != sys.maxsize else -1