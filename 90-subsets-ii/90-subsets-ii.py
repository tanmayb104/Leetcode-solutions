class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l=[[]]
        s=set(tuple([]))
        for i in nums:
            j=len(l)
            while(j):
                a=l[j-1]+[i]
                b=tuple(a)
                if(b not in s):
                    l.append(a)
                    s.add(b)
                j-=1
        return l
        