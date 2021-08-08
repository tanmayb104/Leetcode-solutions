class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1,len(arr)-1):
            if(arr[i-1]<arr[i] and arr[i+1]<arr[i]):
                return i
            