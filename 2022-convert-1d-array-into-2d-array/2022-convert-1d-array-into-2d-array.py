class Solution:
    def construct2DArray(self, l: List[int], m: int, n: int) -> List[List[int]]:
        if(m*n!=len(l)):
            return []
        a=[]
        k=0
        for i in range(m):
            p=[]
            for j in range(n):
                p.append(l[k])
                k+=1
            a.append(p)
        return a
        