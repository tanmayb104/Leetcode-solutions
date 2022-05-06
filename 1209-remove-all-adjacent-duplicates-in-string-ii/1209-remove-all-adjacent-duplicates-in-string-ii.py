class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st=[]
        a=1
        i=0
        while(i<len(s)):
            if(len(st) and a==0):
                a=st[-1][1]
            if(len(st) and s[i]==st[-1][0]):
                a+=1
            else:
                a=1
            if(a==k):
                for j in range(k-1):
                    st.pop()
                i+=1
                a=0
            else:
                st.append([s[i],a])
                i+=1
        ans=""
        for i in st:
            ans+=i[0]
        return ans