class Solution:
    def findMinArrowShots(self, p: List[List[int]]) -> int:
        ans=0
        p=sorted(p,key=lambda x:(x[0],x[1]))
        st=-1
        en=-1
        ans=0
        for i in p:
            if(st==-1):
                st=i[0]
                en=i[1]
            else:
                if(i[0]<=en):
                    st=max(st,i[0])
                    en=min(en,i[1])
                else:
                    ans+=1
                    st=i[0]
                    en=i[1]
        if(st!=-1):
            ans+=1
        return ans
                    
        