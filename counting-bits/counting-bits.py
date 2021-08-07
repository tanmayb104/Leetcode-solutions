from math import log
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0,1,1]
        if(n<3):
            return dp[:n+1]
        a=2
        for i in range(3,n+1):
            if(log(i,2)==int(log(i,2))):
                dp.append(1)
                a=a*2
                continue
            dp.append(dp[i-a]+1)
        return dp