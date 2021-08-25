class Solution:
    def merge(self, l: List[List[int]]) -> List[List[int]]:
        l=sorted(l,key=lambda x:x[0])
        ans=[l[0]]
        for i in range(1,len(l)):
            if(l[i][0]<=ans[-1][1]):
                ans[-1][1]=max(l[i][1],ans[-1][1])
            else:
                ans.append(l[i])
        return ans