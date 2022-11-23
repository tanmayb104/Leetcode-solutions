class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        flag=True
        for i in range(9):
            s=set()
            c=0
            for j in range(9):
                if(b[i][j]!="."):
                    s.add(b[i][j])
                    c+=1
            if(len(s)!=c):
                flag=False
        for j in range(9):
            s=set()
            c=0
            for i in range(9):
                if(b[i][j]!="."):
                    s.add(b[i][j])
                    c+=1
            if(len(s)!=c):
                flag=False
        x=0
        y=0
        for i in range(9):
            s=set()
            c=0
            for j in range(3):
                for k in range(3):
                    if(b[x+j][y+k]!="."):
                        s.add(b[x+j][y+k])
                        c+=1
            if(len(s)!=c):
                flag=False
            y+=3
            if(y%9==0):
                x+=3
                y=0
        return flag
            
                    