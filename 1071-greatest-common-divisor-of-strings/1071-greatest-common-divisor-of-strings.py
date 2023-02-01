class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans=""
        a=""
        for i in range(len(str1)):
            a+=str1[i]
            if(len(str1)%len(a)==0 and len(str2)%len(a)==0):
                if(a*(len(str1)//len(a))==str1 and a*(len(str2)//len(a))==str2):
                    ans=a
        return ans