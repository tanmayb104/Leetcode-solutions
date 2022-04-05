class Solution:
    
    def findpos(self,board,pos):
        avail=set(["1","2","3","4","5","6","7","8","9"])
        taken=set()
        rows={0:[0,1,2],1:[0,1,2],2:[0,1,2],3:[3,4,5],4:[3,4,5],5:[3,4,5],6:[6,7,8],7:[6,7,8],8:[6,7,8]}
        for i in range(9):
            if(board[i][pos[1]]!="."):
                taken.add(board[i][pos[1]])
            if(board[pos[0]][i]!="."):
                taken.add(board[pos[0]][i])
        for i in rows[pos[0]]:
            for j in rows[pos[1]]:
                if(board[i][j]!="."):
                    taken.add(board[i][j])
        possible=avail-taken
        return possible
    
    def findsoln(self,board):
        flag=False
        for i in range(9):
            for j in range(9):
                if(board[i][j]=="."):
                    pos=[i,j]
                    flag=True
                    break
            if(flag):
                break
        if(not flag):
            print(board)
            return board
        possible=self.findpos(board,pos)
        if(not possible):
            return False
        for i in possible:
            board[pos[0]][pos[1]]=i
            a=self.findsoln(board)
            if(not a):
                board[pos[0]][pos[1]]="."
            else:
                return a
        
        
        
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        return self.findsoln(board)