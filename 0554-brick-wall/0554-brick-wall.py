class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d={}
        for i in range(len(wall)):
            for j in range(1,len(wall[i])):
                wall[i][j]+=wall[i][j-1]
            for j in range(len(wall[i])):
                if(wall[i][j] in d):
                    d[wall[i][j]]+=1
                else:
                    d[wall[i][j]]=1
        # print(wall)
        # print(d)
        ans=len(wall)
        for i in d:
            if(i!=wall[0][-1]):
                ans=min(ans,len(wall)-d[i])
        return ans
            