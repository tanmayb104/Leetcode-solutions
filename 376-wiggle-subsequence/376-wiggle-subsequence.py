class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        def calc(prev,flag):
            ans=0
            for i in nums:
                if(flag):
                    if(i>prev):
                        prev=i
                        ans+=1
                        flag=not flag
                    elif(i<prev):
                        prev=i
                else:
                    if(i<prev):
                        prev=i
                        ans+=1
                        flag=not flag
                    elif(i>prev):
                        prev=i
            return ans
        return(max(calc(-1,True),calc(1001,False)))
        