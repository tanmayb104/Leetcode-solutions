class Solution:
    def solve(self,n,board,l,row):
        if(row==n):
            p=[]
            for i in range(n):
                for j in range(n):
                    if(board[i][j]=="0"):
                        board[i][j]="."
                p.append("".join(board[i]))
            self.ans.append(p)
        else:
            for i in range(n):
                if(board[row][i]=="0"):
                    marked=[]
                    for j in range(n):
                        if(board[row][j]=="0"):
                            board[row][j]="."
                            marked.append([row,j])
                        elif(board[row][j]=="Q"):
                            return 
                    for j in range(n):
                        if(board[j][i]=="0"):
                            board[j][i]="."
                            marked.append([j,i])
                    new_r=row+1
                    new_c=i+1
                    while(new_r<n and new_c<n):
                        if(board[new_r][new_c]=="0"):
                            board[new_r][new_c]="."
                            marked.append([new_r,new_c])
                        new_r+=1
                        new_c+=1
                    new_r=row+1
                    new_c=i-1
                    while(new_r<n and new_c>-1):
                        if(board[new_r][new_c]=="0"):
                            board[new_r][new_c]="."
                            marked.append([new_r,new_c])
                        new_r+=1
                        new_c-=1
                    board[row][i]="Q"
                    l.append(marked)
                    self.solve(n,board,l,row+1)
                    board[row][i]="0"
                    p=l.pop()
                    for i in p:
                        board[i[0]][i[1]]="0"
                    
                    
                    
        
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["0" for i in range(n)] for j in range(n)]
        self.ans=[]
        self.solve(n,board,[],0)
        return self.ans