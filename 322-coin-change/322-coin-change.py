class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(maxsize=None)
        def rec(i,a):
            if(a<0):
                return 999999999999
            if(a==0):
                return 0
            if(i==len(coins)-1):
                return 1+rec(i,a-coins[i])
            return min(1+rec(i,a-coins[i]),rec(i+1,a))
        
        a=rec(0,amount)
        if(a>=999999999999):
            return -1
        return a
                