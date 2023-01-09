class Solution:
    def maxPower(self, s: List[int], r: int, k: int) -> int:
        l=[0 for i in range(len(s)+1)]
        for i in range(len(s)):
            mi=max(0,i-r)
            l[mi]+=s[i]
            ma=min(len(s),i+r+1)
            l[ma]-=s[i]
        # for i in range(1,len(l)):
        #     l[i]+=l[i-1]
        le=0
        ri=10**10+10**9
        # print(l)
        while(le<ri):
            mid=ceil((le+ri)/2)
            # print(l,r,mid)
            l1=l.copy()
            s=0
            val=0
            for i in range(len(l1)-1):
                s+=l1[i]
                if(s<mid):
                    val+=mid-s
                    # print(i+2*r+1)
                    if(i+2*r+1<len(l1)):
                        l1[i+2*r+1]-=mid-s
                    s=mid
                # print(l1,i,s,val)
            if(val>k):
                ri=mid-1
            else:
                le=mid
        return le
                    
                        
            
        