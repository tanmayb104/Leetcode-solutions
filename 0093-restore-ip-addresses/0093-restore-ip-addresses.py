class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]
        def rec(st,i,j):
            if(j==3):
                st+=s[i:]
                ans.append(st)
            elif(i==len(s)):
                return s
            else:
                rec(st+"."+s[i],i+1,j+1)
                rec(st+s[i],i+1,j)
        rec(s[0],1,0)
        final=[]
        # print(ans)
        for i in ans:
            # print(i)
            a=i.split(".")
            # print(a)
            flag=True
            for j in a:
                # print(j)
                if (int(j)<0 or 255<int(j) or len(j)!=len(str(int(j)))):
                    flag=False
            if(flag):
                final.append(i)
        return final