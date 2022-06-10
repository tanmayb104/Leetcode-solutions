class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        d={}
        ans=0
        while(r<len(s)):
            if(s[r] not in d):
                d[s[r]]=r
                r+=1
                ans=max(ans,r-l)
            else:
                l=max(l,d[s[r]]+1)
                d[s[r]]=r
                r+=1
                ans=max(ans,r-l)
            # print(d,l,r)
        ans=max(ans,r-l)
        return ans