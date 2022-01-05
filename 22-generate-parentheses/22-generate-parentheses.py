class Solution:
    def rec(self, n, ans, temp, op, cl):
        if(cl==n):
            ans.append(temp)
            return
        if(op==0):
            self.rec(n, ans, temp+"(", 1, cl)
        elif(op+cl<n):
            self.rec(n, ans, temp+"(", op+1, cl)
            self.rec(n, ans, temp+")", op-1, cl+1)
        else:
            self.rec(n, ans, temp+")", op-1, cl+1)
        
        
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        self.rec(n, ans, "", 0, 0)
        return ans