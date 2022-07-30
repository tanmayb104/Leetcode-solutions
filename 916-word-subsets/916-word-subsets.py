class Solution:
    def wordSubsets(self, w1: List[str], w2: List[str]) -> List[str]:
        ans=[]
        d={}
        for i in w2:
            d1={}
            if(len(i)==1):
                if(i in d1):
                    d1[i]+=1
                else:
                    d1[i]=1
            else:
                for j in i:
                    if(j in d1):
                        d1[j]+=1
                    else:
                        d1[j]=1
            for j in d1.keys():
                if(j in d):
                    d[j]=max(d[j],d1[j])
                else:
                    d[j]=d1[j]
        # print(d)
        for i in w1:
            d1=d.copy()
            flag=True
            for j in i:
                if(j in d1):
                    d1[j]-=1
            for j in d1.keys():
                if(d1[j]>0):
                    flag=False
                    break
            if(flag):
                ans.append(i)
        return ans
                    