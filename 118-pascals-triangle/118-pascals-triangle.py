class Solution:
    def generate(self, n: int) -> List[List[int]]:
        l=[[1]]
        for i in range(1,n):
            p=[]
            for j in range(i+1):
                if(j==0):
                    p.append(l[-1][0])
                elif(j==i):
                    p.append(l[-1][-1])
                else:
                    p.append(l[-1][j-1]+l[-1][j])
            l.append(p)
        return l
        