class Solution:
    def equationsPossible(self, e: List[str]) -> bool:
        d={}
        s={}
        for a in e:
            if(a[0] not in d):
                d[a[0]]=a[0]
                s[a[0]]=1
            if(a[3] not in d):
                d[a[3]]=a[3]
                s[a[3]]=1
                
        def find(a):
            if(a!=d[a]):
                d[a]=find(d[a])
            return d[a]
        
        for a in e:
            if(a[1]=="="):
                a1=find(a[0])
                a2=find(a[3])
                if(a1!=a2):
                    if(s[a1]>s[a2]):
                        d[a2]=a1
                        s[a1]+=s[a2]
                    else:
                        d[a1]=a2
                        s[a2]+=s[a1]
                
        for a in e:
            if(a[1]=="!"):
                if(find(a[0])==find(a[3])):
                    return False
        return True
                    