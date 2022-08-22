class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if(n<=0):
            return False
        return int(log(n,4))==log(n,4)