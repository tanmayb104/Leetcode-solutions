class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # check for edge case
        if len(points)<3:
            return len(points)
        
        maxlen = 0
        for i in range(len(points)):
            line = {}
            for j in range(i+1,len(points)):
                y = points[i][1] - points[j][1]
                x = points[i][0] - points[j][0]
                slop = y/x if x!=0 else inf
                
                if slop in line:
                    line[slop]+= 1
                else:
                    line[slop] = 2 
                maxlen = max(line[slop] , maxlen)
        return maxlen