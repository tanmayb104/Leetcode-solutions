class Solution:
    def divide(self, d1: int, d2: int) -> int:
        a=2**31-1
        b=-2**31
        if((d1>0 and d2>0) or (d1<0 and d2<0)):
            q=abs(d1)//abs(d2)
        elif(d2==0):
            if(d1<0):
                q=b
            else:
                q=a
        else:
            q=-(abs(d1)//abs(d2))
        if(q>a):
            return a
        elif(q<b):
            return b
        return q