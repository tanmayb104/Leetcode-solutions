class Solution:
    def minMoves2(self, n: List[int]) -> int:
        n.sort()
        if(len(n)%2==1):
            mid=len(n)//2
            ans=0
            for i in range(len(n)):
                ans+=abs(n[mid]-n[i])
            return ans
        else:
            mid1=len(n)//2
            mid2=len(n)//2-1
            ans1=0
            ans2=0
            for i in range(len(n)):
                ans1+=abs(n[mid1]-n[i])
                ans2+=abs(n[mid2]-n[i])
            return min(ans1,ans2)
            