class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=[[]]
        for i in nums:
            j=len(l)
            while(j):
                l.append(l[j-1]+[i])
                j-=1
        return l