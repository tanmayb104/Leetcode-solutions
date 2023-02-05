class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=0
        r=0
        c=Counter(p)
        ans=[]
        while(r<len(s)):
            # print(l,r,c)
            if(r-l==len(p)):
                ans.append(l)
                if(s[r] in c and c[s[r]]):
                    c[s[r]]-=1
                    r+=1
                c[s[l]]+=1
                l+=1
            else:
                if(s[r] in c and c[s[r]]):
                    c[s[r]]-=1
                    r+=1
                else:
                    c[s[l]]+=1
                    l+=1
        if(r-l==len(p)):
            ans.append(l)
        return ans
                
                