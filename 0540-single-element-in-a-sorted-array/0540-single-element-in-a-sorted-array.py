class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        r=len(nums)
        while(l<r):
            mid=(l+r)//2
            if(mid%2==0):
                if(mid+1<len(nums)):
                    if(nums[mid]==nums[mid+1]):
                        l=mid+2
                    elif(nums[mid]==nums[mid-1]):
                        r=mid-1
                    else:
                        return nums[mid]
                elif(nums[mid]==nums[mid-1]):
                    r=mid-1
                else:
                    return nums[mid]
            else:
                if(mid+1<len(nums)):
                    if(nums[mid]==nums[mid+1]):
                        r=mid
                    elif(nums[mid]==nums[mid-1]):
                        l=mid+1
                    else:
                        return nums[mid]
                elif(nums[mid]==nums[mid-1]):
                    l=mid+1
                else:
                    return nums[mid]
        return nums[l]