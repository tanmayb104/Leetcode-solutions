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
        for i in p.keys():
            n[i]=[]
        for i in range(len(s)):
            a=find_set(i)
            n[a].append(s[i])
        for i in n.keys():
            n[i].sort(reverse=True)
        ans=""
        for i in range(len(s)):
            a=find_set(i)
            ans+=n[a].pop()
        return ans
                
        
        