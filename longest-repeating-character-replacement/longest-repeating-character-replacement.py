from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=k
        ans=0
        d=Counter(s[:k])
        while(r<len(s)):
            if(len(d)):
                a=d.most_common(1)[0][1]
                if(k>=r-l-a):
                    if(s[r] in d):
                        d[s[r]]+=1
                    else:
                        d[s[r]]=1
                    ans=max(ans,r-l)
                    r+=1
                else:
                    d[s[l]]-=1
                    l+=1
            else:
                if(s[r] in d):
                    d[s[r]]+=1
                else:
                    d[s[r]]=1
                ans=max(ans,r-l)
                r+=1
        a=d.most_common(1)[0][1]
        if(k>=r-l-a):
            ans=max(ans,r-l)
        return ans
        
                    
            