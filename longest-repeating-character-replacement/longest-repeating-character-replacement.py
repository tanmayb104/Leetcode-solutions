from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        ans=0
        d={}
        for i in range(65,91):
            d[chr(i)]=0
        while(r<len(s)):
            a=0
            for i in range(65,91):
                a=max(d[chr(i)],a)
            # print(l,r,a)
            if(k>=r-l-a):
                d[s[r]]+=1
                ans=max(ans,r-l)
                r+=1
            else:
                d[s[l]]-=1
                l+=1
        a=0
        for i in range(65,91):
            a=max(d[chr(i)],a)
        if(k>=r-l-a):
            ans=max(ans,r-l)
        return ans
        
                    
            