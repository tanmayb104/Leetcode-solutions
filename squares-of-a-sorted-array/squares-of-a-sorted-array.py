class Solution:
    def sortedSquares(self, l1: List[int]) -> List[int]:
        l2=[]
        flag=1
        for i in range(len(l1)):
            if(l1[i]<0):
                l2.append(abs(l1[i]))
            else:
                flag=0
                break
        if(flag==0):
            l1=l1[i:]
        else:
            l1=[]
        l=[]
        i=0
        j=0
        l2.reverse()
        print(l1,l2)
        while(i<len(l1) and j<len(l2)):
            if(l2[j]<l1[i]):
                l.append(l2[j]*l2[j])
                j+=1
            else:
                l.append(l1[i]*l1[i])
                i+=1
        while(i<len(l1)):
            l.append(l1[i]*l1[i])
            i+=1
        while(j<len(l2)):
            l.append(l2[j]*l2[j])
            j+=1
        return l
        