class Solution:
    def subsets(self, s: List[int]) -> List[List[int]]:
        l=[[]]
        for i in s:
            j=len(l)
            while(j):
                l.append(l[j-1]+[i])
                j-=1
        return l