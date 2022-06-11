from bisect import *
class Solution:
    def minOperations(self, n: List[int], x: int) -> int:
        ans=-1
        pre=[0]
        for i in range(len(n)):
            pre.append(pre[-1]+n[i])
        post=[pre[-1]]
        for i in range(len(n)):
            post.append(post[-1]-n[i])
        # print(n)
        # print(pre)
        # print(post)
        for i in range(len(n),-1,-1):
            a=x-post[i]
            b=bisect_left(pre,a)
            if(b>-1 and b<len(pre) and pre[b]==a):
                # print(b,i)
                po=b+len(n)-i
                if(po<=len(n)):
                    if(ans==-1):
                        ans=b+len(n)-i
                    else:
                        ans=min(ans,b+len(n)-i)
        return ans