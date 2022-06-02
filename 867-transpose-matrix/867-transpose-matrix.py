class Solution:
    def transpose(self, ma: List[List[int]]) -> List[List[int]]:
        n=len(ma)
        m=len(ma[0])
        p=[[-1 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                p[i][j]=ma[j][i]
        return p