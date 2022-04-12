from bisect import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr=sorted(arr,key=lambda a:abs(a-x))
        return sorted(arr[:k])