class Solution:
    def mergesort(self,nums):
        if(len(nums)==1):
            return nums
        else:
            mid=len(nums)//2
            l1=self.mergesort(nums[:mid])
            l2=self.mergesort(nums[mid:])
            l=[]
            i=0
            j=0
            while(i<len(l1) and j<len(l2)):
                if(l1[i]<=l2[j]):
                    l.append(l1[i])
                    i+=1
                else:
                    l.append(l2[j])
                    j+=1
            while(i<len(l1)):
                l.append(l1[i])
                i+=1
            while(j<len(l2)):
                l.append(l2[j])
                j+=1
            return l
                
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergesort(nums)
        