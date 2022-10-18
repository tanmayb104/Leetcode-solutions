class Solution:
    def countAndSay(self, n: int) -> str:
        j=1
        ans="1"
        while(j!=n):
            a=""
            c=1
            for i in range(1,len(ans)):
                if(ans[i]!=ans[i-1]):
                    a+=str(c)
                    a+=ans[i-1]
                    c=1
                else:
                    c+=1
            a+=str(c)
            a+=ans[-1]
            j+=1
            ans=a
            # print(ans)
        return ans
            