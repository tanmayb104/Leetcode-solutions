class Solution:
    def eraseOverlapIntervals(self, i: List[List[int]]) -> int:
        if(len(i)==1):
            return 0
        i=sorted(i,key=lambda x:(x[0],x[1]))
        # print(i)
        c=0
        j=0
        k=1
        while(k<len(i)):
            if(i[k][0]<i[j][1]):
                if(i[k][1]>=i[j][1]):
                    c+=1
                    k+=1
                else:
                    c+=1
                    j=k
                    k+=1
            else:
                j=k
                k+=1
        return c