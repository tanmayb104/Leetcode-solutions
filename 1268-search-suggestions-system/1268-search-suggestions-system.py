class Solution:
    def suggestedProducts(self, p: List[str], sw: str) -> List[List[str]]:
        # print(p)
        p.sort()
        ans=[]
        s=""
        for i in range(len(sw)):
            s+=sw[i]
            # print(s)
            l=0
            r=len(p)
            t=[]
            while(l<r):
                mid=(l+r)//2
                if(p[mid]<s):
                    l=mid+1
                else:
                    r=mid
            pl=l+3
            while(l<len(p) and l<pl and len(p[l])>=len(s) and p[l][:len(s)]==s):
                t.append(p[l])
                l+=1
            ans.append(t)
        return ans
                # elif(len(p[mid])>=len(s) and p[mid][:len(s)]==s):
                #     r=mid