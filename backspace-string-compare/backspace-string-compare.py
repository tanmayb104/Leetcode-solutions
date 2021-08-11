class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st=[]
        for i in s:
            if(i=="#"):
                if(len(st)):
                    st.pop()
            else:
                st.append(i)
        s=st
        st=[]
        for i in t:
            if(i=="#"):
                if(len(st)):
                    st.pop()
            else:
                st.append(i)
        if(s==st):
            return 1
        return 0