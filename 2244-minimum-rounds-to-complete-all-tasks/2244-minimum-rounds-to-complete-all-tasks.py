class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c=Counter(tasks)
        for i in c:
            if(c[i]==1):
                return -1
        ans=0
        for i in c:
            ans+=c[i]//3
            ans+=ceil((c[i]%3)/2)
        return ans