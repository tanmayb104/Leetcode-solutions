class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[["!",0]]
        ans=0
        for i in range(len(s)):
            if(s[i]=="("):
                st.append([s[i],0])
            else:
                if(st[-1][0]=="("):
                    a,b=st.pop()
                    st[-1][1]+=2+b
                else:
                    ans=max(ans,st[-1][1])
                    st=[["!",0]]
        for i in range(len(st)):
            ans=max(ans,st[i][1])
        # print(ans)
        return ans