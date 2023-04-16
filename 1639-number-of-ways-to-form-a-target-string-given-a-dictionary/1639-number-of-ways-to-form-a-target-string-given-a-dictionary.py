from collections import defaultdict
class Solution:
    def numWays(self, words: List[str], t: str) -> int:
        d={}
        for i in range(len(words[0])):
            d[i]={}
            for j in words:
                if(j[i] not in d[i]):
                    d[i][j[i]]=1
                else:
                    d[i][j[i]]+=1
                    
        def rec(i,j):
            tu=tuple([i,j])
            if(tu in ca):
                return ca[tu]
            if(i==len(t)):
                return 1
            elif(j==len(words[0])):
                return 0
            b=rec(i,j+1)
            a=0
            if(t[i] in d[j]):
                a=rec(i+1,j+1)*d[j][t[i]]
            # print(i,j,t[i],a,b)
            ca[tu]=a+b
            return ca[tu]
        ca={}
        return rec(0,0)%1000000007
        
        
                