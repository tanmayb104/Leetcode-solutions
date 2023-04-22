class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def rec(l,r):
            if(l<r):
                if(s[l]==s[r]):
                    return rec(l+1,r-1)
                else:
                    return min(1+rec(l,r-1),1+rec(l+1,r))
            else:
                return 0
        return rec(0,len(s)-1)