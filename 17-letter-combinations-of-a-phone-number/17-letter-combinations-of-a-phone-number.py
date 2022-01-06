class Solution:
    def rec(self,digits,d,s,ans,i):
        if(i==len(digits)):
            ans.append(s)
        else:
            for j in d[digits[i]]:
                self.rec(digits,d,s+j,ans,i+1)
    def letterCombinations(self, digits: str) -> List[str]:
        d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        s=""
        ans=[]
        if(len(digits)):
            self.rec(digits,d,s,ans,0)
        return ans