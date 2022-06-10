class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        d={}
        ans=0
        while(r<len(s)):
            if(s[r] not in d):
                d[s[r]]=1
                r+=1
                ans=max(ans,r-l)
            else:
                while(s[r]!=s[l]):
                    del d[s[l]]
                    l+=1
                del d[s[l]]
                l+=1
        ans=max(ans,r-l)
        return ans