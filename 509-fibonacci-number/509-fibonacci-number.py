class Solution:
    def fib(self, n: int) -> int:
        if(n==0 or n==1):
            return n
        a=0
        b=1
        while(n-1):
            c=a+b
            a,b=b,c
            n-=1
        return c