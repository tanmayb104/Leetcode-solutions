class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_nums = [nums[0]]
        for i in range(1, len(nums)):
            min_nums.append(min(nums[i], min_nums[-1]))
            
        st = []  
        i = len(nums) - 1
        for i in range(len(nums)-1, 0, -1):
            if(nums[i]>min_nums[i-1]):
                if(not st):
                    st.append(nums[i])
                else:
                    while(st and st[-1]<=min_nums[i-1]):
                        st.pop()
                    if(st and st[-1]<nums[i]):
                        return True
                    else:
                        st.append(nums[i])
        return False 