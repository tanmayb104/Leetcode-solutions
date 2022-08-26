class Solution:
    def reorderedPowerOf2(self, num: int) -> bool:
        n=1
        s=set()
        while(n<=10**9):
            st="".join(sorted(str(n),reverse=True))
            s.add(st)
            n*=2
        so="".join(sorted(str(num),reverse=True))
        return so in s