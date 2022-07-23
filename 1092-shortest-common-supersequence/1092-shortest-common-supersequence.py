class Solution:
    def shortestCommonSupersequence(self, t1: str, t2: str) -> str:
        d={}
        def rec(i1,i2):
            tu=tuple([i1,i2])
            if(i1==len(t1) or i2==len(t2)):
                return 0
            if(tu in d):
                return d[tu][0]
            if(t1[i1]==t2[i2]):
                d[tu]=[1+rec(i1+1,i2+1),0]
                return d[tu][0]
            a=rec(i1+1,i2)
            b=rec(i1,i2+1)
            if(a>b):
                d[tu]=[a,1]
            else:
                d[tu]=[b,-1]
            return d[tu][0]
        rec(0,0)
        i1=0
        i2=0
        ans=""
        while(i1<len(t1) and i2<len(t2)):
            if(t1[i1]==t2[i2]):
                ans+=t1[i1]
                i1+=1
                i2+=1
            else:
                tu=tuple([i1,i2])
                if(d[tu][1]==1):
                    i1+=1
                else:
                    i2+=1
        i1=0
        i2=0
        i3=0
        fans=""
        # print(t1,t2,ans)
        while(i1<len(t1) and i2<len(t2) and i3<len(ans)):
            if(t1[i1]==t2[i2] and t2[i2]==ans[i3]):
                fans+=t1[i1]
                i1+=1
                i2+=1
                i3+=1
            elif(t1[i1]==ans[i3]):
                fans+=t2[i2]
                i2+=1
            elif(t2[i2]==ans[i3]):
                fans+=t1[i1]
                i1+=1
            else:
                fans+=t1[i1]
                i1+=1
                fans+=t2[i2]
                i2+=1
        while(i1<len(t1)):
            fans+=t1[i1]
            i1+=1
        while(i2<len(t2)):
            fans+=t2[i2]
            i2+=1
        return fans