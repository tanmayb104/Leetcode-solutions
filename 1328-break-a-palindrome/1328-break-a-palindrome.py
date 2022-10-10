class Solution:
    def breakPalindrome(self, p: str) -> str:
        flag=False
        for i in range(len(p)):
            if(p[i]!="a"):
                flag=True
                break
        if(flag and i!=len(p)//2):
            return p[:i]+"a"+p[i+1:]
        if(len(p)==1):
            return ""
        return p[:-1]+"b"