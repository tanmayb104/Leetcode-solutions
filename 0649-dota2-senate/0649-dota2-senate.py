from collections import deque
class Solution:
    def predictPartyVictory(self, sen: str) -> str:
        r=0
        d=0
        q=deque([])
        for i in sen:
            q.append(i)
        while(r<len(sen) and d<len(sen)):
            a=q.popleft()
            if(a=="R"):
                if(r>0):
                    r-=1
                else:
                    d+=1
                    q.append(a)
            else:
                if(d>0):
                    d-=1
                else:
                    r+=1
                    q.append(a)
        if(r):
            return "Dire"
        else:
            return "Radiant"
                    