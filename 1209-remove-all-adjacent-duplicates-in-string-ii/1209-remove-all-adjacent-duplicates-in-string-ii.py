class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st=[["!$",0]]
        i=0
        while(i<len(s)):
            # print(st)
            if(st[-1][0]==s[i]):
                st[-1][1]+=1
                if(st[-1][1]==k):
                    st.pop()
            else:
                st.append([s[i],1])
            i+=1
        ans=""
        for i in st:
            ans+=i[0]*i[1]
        return ans