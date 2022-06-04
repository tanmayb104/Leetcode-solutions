class Solution:
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["." for i in range(n)] for j in range(n)]
        vis=[[0 for i in range(n)] for j in range(n)]
        self.ans=[]
        
        def rec(i,l):
            # print(board)
            # print(vis)
            # print(i,l)
            # print("****88",self.ans)
            if(i==n):
                p=[]
                for i in range(n):
                    o=""
                    for j in board[i]:
                        o+=j
                    p.append(o)
                self.ans.append(p)
                return
            else:
                for j in range(n):
                    if(vis[i][j]==0):
                        board[i][j]="Q"
                        attack=[]
                        a=i+1
                        b=j+1
                        c=j-1
                        while(a<n):
                            if(b<n):
                                attack.append([a,b])
                                vis[a][b]+=1
                                b+=1
                            attack.append([a,j])
                            vis[a][j]+=1
                            if(c>-1):
                                attack.append([a,c])
                                vis[a][c]+=1
                                c-=1
                            a+=1
                        l.append(attack)
                        rec(i+1,l)
                        at=l.pop()
                        for k in at:
                            vis[k[0]][k[1]]-=1
                        board[i][j]="."
        rec(0,[])
        return self.ans