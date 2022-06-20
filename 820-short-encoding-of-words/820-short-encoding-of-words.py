class Solution:
    def minimumLengthEncoding(self, w: List[str]) -> int:
        w=sorted(w,key=lambda x:len(x),reverse=True)
        ans=0
        for i in range(len(w)):
            f=0
            for j in range(0,i):
                if(w[j][len(w[j])-len(w[i]):]==w[i]):
                    f=1
                    break
            if(not f):
                ans+=len(w[i])+1
        return ans