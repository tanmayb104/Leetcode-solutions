class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n=len(nums1)
        l=[]
        for i in range(n):
            l.append([nums1[i],nums2[i]])
        l=sorted(l,key=lambda x:(x[1],x[0]),reverse=True)
        h=[]
        heapify(h)
        ans=0
        tot=0
        for i in range(n):
            tot+=l[i][0]
            heappush(h,l[i][0])
            if(len(h)>k):
                tot-=heappop(h)
            if(len(h)==k):
                ans=max(ans,tot*l[i][1])
        return ans