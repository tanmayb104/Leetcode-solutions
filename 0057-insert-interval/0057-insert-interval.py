class Solution:
    def insert(self, l: List[List[int]], n: List[int]) -> List[List[int]]:
        l+=[n]
        l=sorted(l,key=lambda x:x[0])
        # print(l)
        ans=[]
        for i in range(len(l)):
            if(not ans):
                ans.append(l[i])
            else:
                if(ans[-1][1]>=l[i][0]):
                    ans[-1][1]=max(ans[-1][1],l[i][1])
                else:
                    ans.append(l[i])
        return ans