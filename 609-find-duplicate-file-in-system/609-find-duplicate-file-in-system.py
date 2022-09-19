class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d={}
        for i in paths:
            a=i.split(" ")
            for j in range(1,len(a)):
                b=a[j].split("(")
                c=b[1][:-1]
                if(c in d):
                    d[c].append(a[0]+"/"+b[0])
                else:
                    d[c]=[a[0]+"/"+b[0]]
        ans=[]
        for i in d:
            if(len(d[i])>1):
                ans.append(d[i])
        return ans