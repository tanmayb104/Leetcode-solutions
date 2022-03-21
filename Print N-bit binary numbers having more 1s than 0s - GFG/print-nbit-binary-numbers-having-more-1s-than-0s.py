#User function Template for python3
class Solution:
	def NBitBinary(self, n):
		# code here
		l=[]
		s=""
		def rec(n,s,one,zero):
		    if(one+zero==n):
		        l.append(s)
		        return 
		    if(one==zero):
		        rec(n,s+"1",one+1,zero)
		    else:
		        rec(n,s+"1",one+1,zero)
		        rec(n,s+"0",one,zero+1)
	    rec(n,s,0,0)
	    return l
	    
		
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends