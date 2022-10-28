class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        d={}
        for i in s:
            a="".join(sorted(i))
            if(a in d):
                d[a].append(i)
            else:
                d[a]=[i]
        ans=[]
        for i in d:
            ans.append(d[i])
        return ans