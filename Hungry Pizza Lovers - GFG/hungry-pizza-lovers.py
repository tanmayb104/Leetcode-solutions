#User function Template for python3

class Solution:
    def permute(self,arr,n):
        #Complete the function
        arr=[[i,arr[i][0]+arr[i][1]] for i in range(n)]
        arr=sorted(arr,key=lambda x:x[1])
        return [i[0]+1 for i in arr]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

    
for _ in range(0,int(input())):
    n = int(input())
    arr = []
    for _ in range(0, n):
        ll = list(map(int, input().strip().split()))
        arr.append(ll)
    obj=Solution()
    ans = obj.permute(arr, n)
    for i in ans:
        print(i)
    



# } Driver Code Ends