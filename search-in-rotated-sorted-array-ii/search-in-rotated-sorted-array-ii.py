class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return True
            temp=low
            while(nums[low]==nums[mid] and low>=0):
                low-=1
            if low==-1:
                low=temp+1
                continue
            if nums[low] < nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False