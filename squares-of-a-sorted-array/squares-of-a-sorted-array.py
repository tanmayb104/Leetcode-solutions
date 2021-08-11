class Solution:
    def sortedSquares(self, l1: List[int]) -> List[int]:
        return(sorted([i*i for i in l1]))