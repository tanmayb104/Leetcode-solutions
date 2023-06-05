class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        s=0
        sl=-1
        for i in range(len(c)-1):
            if(c[i][1]-c[i+1][1]==0):
                s+=1
            else:
                if(sl==-1):
                    sl=(c[i][0]-c[i+1][0])/(c[i][1]-c[i+1][1])
                elif(sl!=(c[i][0]-c[i+1][0])/(c[i][1]-c[i+1][1])):
                    return False
        if(s==0 or s==len(c)-1):
            return True
        return False