class Solution:
    def maxProduct(self, w: List[str]) -> int:
        d={}
        for i in range(len(w)):
            d[i]=set([i for i in w[i]])
        m=0
        for i in range(len(w)-1):
            for j in range(i+1,len(w)):
                if(not d[i].intersection(d[j])):
                    m=max(m,len(w[i])*len(w[j]))
        return m