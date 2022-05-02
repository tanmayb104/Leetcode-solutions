#User function Template for python3

class Solution:
    def partyHouse(self, N, adj):
        # code here
        ans=99999999999
        for i in range(1,N+1):
            st=[[i,0]]
            vis=set()
            temp=0
            while(st):
                a,b=st.pop()
                vis.add(a)
                temp=max(temp,b)
                for j in adj[a]:
                    if(j not in vis):
                        st.append([j,b+1])
            ans=min(ans,temp)
        return ans
                    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        adj = [[] for x in range(N+1)]
        for i in range(N-1):
            x, y = [int(a) for a in input().split()]
            adj[x].append(y)
            adj[y].append(x)
        
        ob = Solution()
        print(ob.partyHouse(N, adj))
# } Driver Code Ends