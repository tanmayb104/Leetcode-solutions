class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i=0
        while(coins and i<len(costs)):
            if(costs[i]<=coins):
                coins-=costs[i]
                i+=1
            else:
                break
        return i