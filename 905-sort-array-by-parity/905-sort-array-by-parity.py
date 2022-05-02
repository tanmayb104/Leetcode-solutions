class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        for i in nums:
            if(i%2):
                b.append(i)
            else:
                a.append(i)
        return a+b