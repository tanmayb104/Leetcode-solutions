class Solution:
    def checkPossibility(self, n: List[int]) -> bool:
        l=[]
        for i in range(1,len(n)):
            if(n[i-1]>n[i]):
                l.append(i)
        print(l)
        if(len(l)==0):
            return True
        if(len(l)>1):
            return False
        if(l[0]==1 or l[0]==len(n)-1):
            return True
        else:
            if(n[l[0]-2]<=n[l[0]] or n[l[0]-1]<=n[l[0]+1]):
                return True
            return False