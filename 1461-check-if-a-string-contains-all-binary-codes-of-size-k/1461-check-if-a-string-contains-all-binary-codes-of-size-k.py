class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        se=set()
        for i in range(k,len(s)+1):
            se.add(s[i-k:i])
        return True if len(se)==2**k else False