class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={}
        for i in range(len(order)):
            d[order[i]]=chr(ord("a")+i)
        l=[]
        for i in words:
            a=""
            for j in i:
                a+=d[j]
            l.append(a)
        return l==sorted(l)