#User function Template for python3

class Solution:

    def candyStore(self, candies,N,K):
        # code here
        candies.sort()
        l=0
        r=N-1
        a1=0
        while(l<=r):
            a1+=candies[l]
            l+=1
            r-=K
        l=0
        r=N-1
        a2=0
        while(l<=r):
            a2+=candies[r]
            l+=K
            r-=1
        return [a1,a2]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        N,K = [int(x) for x in input().split()]
        candies = [int(x) for x in input().split()]

        solObj = Solution()

        print(*solObj.candyStore(candies,N,K))
# } Driver Code Ends