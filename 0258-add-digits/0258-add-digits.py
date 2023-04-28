class Solution:
    def addDigits(self, num: int) -> int:
        if(len(str(num))==1):
            return num
        ans=0
        for i in str(num):
            ans+=int(i)
        return self.addDigits(ans)