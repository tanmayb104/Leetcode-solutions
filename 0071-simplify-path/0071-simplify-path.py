class Solution:
    def simplifyPath(self, path: str) -> str:
        s=path.split("/")
        st=[]
        for i in s:
            if(i=="" or i=="."):
                pass
            elif(i==".."):
                if(st):
                    st.pop()
            else:
                st.append(i)
        return "/"+"/".join(st)