def check(b,i,j,p,word,c):
    if(p==len(word)):
        return True
    x1,x2,x3,x4=False,False,False,False
    if(i+1<len(b) and b[i+1][j]==word[p] and c[i+1][j]==-1):
        c[i+1][j]=1
        x1=check(b,i+1,j,p+1,word,c)
        c[i+1][j]=-1
    if(i-1>-1 and b[i-1][j]==word[p] and c[i-1][j]==-1):
        c[i-1][j]=1
        x2=check(b,i-1,j,p+1,word,c)
        c[i-1][j]=-1
    if(j+1<len(b[0]) and b[i][j+1]==word[p] and c[i][j+1]==-1):
        c[i][j+1]=1
        x3=check(b,i,j+1,p+1,word,c)
        c[i][j+1]=-1
    if(j-1>-1 and b[i][j-1]==word[p] and c[i][j-1]==-1):
        c[i][j-1]=1
        x4=check(b,i,j-1,p+1,word,c)
        c[i][j-1]=-1
    return x1|x2|x3|x4

class Solution:
    def exist(self, b: List[List[str]], word: str) -> bool:
        c=[[-1 for i in range(len(b[0]))] for i in range(len(b))]
        
        for i in range(len(b)):
            for j in range(len(b[0])):
                if(b[i][j]==word[0]):
                    c[i][j]=1
                    a=check(b,i,j,1,word,c)
                    if(a):
                        return a
                    else:
                        c[i][j]=-1
        return False
                        