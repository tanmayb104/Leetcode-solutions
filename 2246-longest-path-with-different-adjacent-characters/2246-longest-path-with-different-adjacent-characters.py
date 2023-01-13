class Solution:
    def longestPath(self, par: List[int], s: str) -> int:
        dit = {}
        for i in range(len(par)):
            if par[i] in dit:
                dit[par[i]].append(i)
            else:
                dit[par[i]] = [i]
                
        ans = 1        
        def dfs(n):
            nonlocal ans
            if n not in dit:
                return 1
            
            largest=0 
            second_largest=0 
            for u in dit[n]:
                curr = dfs(u)
                if s[u]!=s[n]:
                    if curr>largest:
                        second_largest = largest
                        largest = curr
                    elif curr>second_largest:
                        second_largest = curr
                        
            ans = max(ans,largest+second_largest+1) 
            return largest+1  
        
        dfs(0)
        return ans