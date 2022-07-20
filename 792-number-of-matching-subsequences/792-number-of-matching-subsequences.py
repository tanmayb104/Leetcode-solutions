
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans=0
        c=Counter(words)
        for w in c.keys():
            i=0
            for j in s:
                if(i==len(w)):
                    break
                elif(i<len(w) and j==w[i]):
                    i+=1
            if(i==len(w)):
                ans+=c[w]
        return ans