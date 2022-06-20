class Solution:
    def minimumLengthEncoding(self, w: List[str]) -> int:
        w.sort(key=len,reverse=True) 
        ans=''
        for x in w:
            if x+'#' not in ans: 
                ans+=x+'#'
        return len(ans)