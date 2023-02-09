class Solution:
    def distinctNames(self, i: List[str]) -> int:
        total=0
        s=set(i)
        d={}
        for i in s:
            if(i[0] in d):
                d[i[0]].add(i[1:])
            else:
                d[i[0]]=set([i[1:]])
        ans=0
        for i in d.keys():
            for j in d.keys():
                if(i!=j):
                    s1=d[i]-d[j]
                    s2=d[j]-d[i]
                    ans+=len(s1)*len(s2)
        return ans