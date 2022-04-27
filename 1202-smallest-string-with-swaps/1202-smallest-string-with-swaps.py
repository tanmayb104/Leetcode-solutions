class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        p={}
        r={}
        for i in range(len(s)):
            p[i]=i
            r[i]=1
        print(p)
        def find_set(a):
            if(a==p[a]):
                return a
            p[a]=find_set(p[a])
            return p[a]
        
        def union_set(a,b):
            a=find_set(a)
            b=find_set(b)
            if(a!=b):
                if(r[a]<r[b]):
                    a,b=b,a
                p[b]=a
                r[a]+=r[b]
        
        for i in pairs:
            union_set(i[0],i[1])
        
        n={}
        m={}
        for i in range(len(s)):
            a=i
            while(a!=p[a]):
                a=p[a]
            if(a in n):
                n[a].append(s[i])
                m[a].append(i)
            else:
                n[a]=[s[i]]
                m[a]=[i]
        for i in n.keys():
            n[i].sort()
            m[i].sort()
        l=[]
        for i in n.keys():
            for j in range(len(n[i])):
                l.append([m[i][j],n[i][j]])
        l.sort()
        ans=""
        for i in l:
            ans+=i[1]
        return ans
            
                
        
        