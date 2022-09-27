class Solution:
    def pushDominoes(self, d: str) -> str:
        l=[[".",0] for i in range(len(d))]
        flag=False
        t=0
        for i in range(len(d)):
            if(d[i]=="."):
                if(not flag):
                    l[i]=[".",0]
                else:
                    l[i]=["R",t]
                    t+=1
            elif(d[i]=="R"):
                flag=True
                t=1
                l[i]=["R",0]
            else:
                l[i]=["L",0]
                flag=False
                t=0
        # print(l)
        flag=False
        t=0
        for i in range(len(d)-1,-1,-1):
            if(d[i]=="."):
                if(not flag):
                    pass
                else:
                    if(l[i][0]=="."):
                        l[i]=["L",t]
                        t+=1
                    elif(l[i][0]=="R"):
                        if(l[i][1]>t):
                            l[i]=["L",t]
                            t+=1
                        elif(l[i][1]==t):
                            l[i]=[".",0]
                            t=0
                            flag=False
                        else:
                            t=0
                            flag=False
            elif(d[i]=="L"):
                flag=True
                t=1
                l[i]=["L",0]
            else:
                flag=False
                t=0
        
        s=""
        for i in l:
            s+=i[0]
        return s
        