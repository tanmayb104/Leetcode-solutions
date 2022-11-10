class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]
        for i in s:
            if(not st):
                st.append(i)
            else:
                if(st[-1]==i):
                    st.pop()
                else:
                    st.append(i)
        return "".join(st)