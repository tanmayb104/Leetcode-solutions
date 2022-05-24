class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[0]
        ans=0
        for i in range(len(s)):
            if(s[i]=="("):
                st.append(0)
            else:
                if(len(st)>1):
                    val=st.pop()
                    st[-1]+=2+val
                else:
                    ans=max(ans,st[-1])
                    st=[0]
        a=max(st)
        return max(ans,a)