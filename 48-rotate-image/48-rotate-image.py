from math import ceil
class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(m)
        j=n-1
        for i in range(n//2):
            k=i
            while(k<j):
                print(i,k)
                if(i==k):
                    m[i][i],m[i][n-i-1],m[n-i-1][n-i-1],m[n-i-1][i]=m[n-i-1][i],m[i][i],m[i][n-i-1],m[n-i-1][n-i-1]
                else:
                    m[i][k],m[k][n-i-1],m[n-i-1][n-k-1],m[n-k-1][i]=m[n-k-1][i],m[i][k],m[k][n-i-1],m[n-i-1][n-k-1]
                k+=1
            j-=1
        # print(m)
                
            