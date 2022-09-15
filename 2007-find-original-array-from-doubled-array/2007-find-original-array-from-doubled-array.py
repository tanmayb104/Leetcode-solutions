class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ans=[]
        d={}
        changed.sort()
        for i in changed:
            if(i%2==0 and i//2 in d and d[i//2]>0):
                d[i//2]-=1
                ans.append(i//2)
            elif(i in d):
                d[i]+=1
            else:
                d[i]=1
            # print(d)
        for i in d:
            if(d[i]!=0):
                ans=[]
        return ans