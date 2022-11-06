class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if(k==1):
            mi=s
            for i in range(len(s)):
                s=s[1:]+s[0]
                mi=min(s,mi)
            return mi
        return "".join(sorted(s))