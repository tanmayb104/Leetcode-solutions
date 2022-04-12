from bisect import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        a=bisect_left(arr,x)
        l=a-1
        r=a
        while(k and l>-1 and r<len(arr)):
            if(abs(arr[l]-x)<=abs(arr[r]-x)):
                l-=1
            else:
                r+=1
            k-=1
        if(k):
            while(k and l>-1):
                l-=1
                k-=1
            while(k and r<len(arr)):
                r+=1
                k-=1
        return arr[l+1:r]