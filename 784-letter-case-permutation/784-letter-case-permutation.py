class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        l=['']
        for i in s:
            if((ord(i)>64 and ord(i)<91) or (ord(i)>96 and ord(i)<123)):
                t=[]
                for j in range(len(l)):
                    a=i.lower()
                    b=i.upper()
                    t.append(l[j]+b)
                    l[j]+=a
                l+=t
            else:
                for j in range(len(l)):
                    l[j]+=i
        return l
                