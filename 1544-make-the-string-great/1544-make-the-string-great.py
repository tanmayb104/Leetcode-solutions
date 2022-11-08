class Solution:
    def makeGood(self, s: str) -> str:
        st=[]
        for i in range(len(s)):
            if(not st):
                st.append(s[i])
            else:
                if(st[-1].upper()==s[i].upper() and st[-1]!=s[i]):
                    st.pop()
                else:
                    st.append(s[i])
        return "".join(st)
                
            