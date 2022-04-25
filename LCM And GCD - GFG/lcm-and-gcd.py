#User function Template for python3

class Solution:
    def gcd(self,a,b):
        if(a>b):
            a,b=b,a
        if(a==0):
            return b
        else:
            return self.gcd(a,b%a)
    def lcmAndGcd(self, A , B):
        # code here 
        a=self.gcd(A,B)
        return([A*B//a,a])

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends