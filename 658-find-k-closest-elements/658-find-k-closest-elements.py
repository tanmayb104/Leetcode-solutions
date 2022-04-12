from bisect import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        a=bisect_left(arr,x)
        ans=[]
        l=a-1
        r=a
        while(k and l>-1 and r<len(arr)):
            if(abs(arr[l]-x)<=abs(arr[r]-x)):
                ans.append(arr[l])
                l-=1
            else:
                ans.append(arr[r])
                r+=1
            k-=1
        if(k):
            while(k and l>-1):
                ans.append(arr[l])
                l-=1
                k-=1
            while(k and r<len(arr)):
                ans.append(arr[r])
                r+=1
                k-=1
        return sorted(ans)