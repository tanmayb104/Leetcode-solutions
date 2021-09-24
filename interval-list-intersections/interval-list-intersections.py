class Solution:
    def intervalIntersection(self, f: List[List[int]], s: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        ans=[]
        while(i<len(f) and j<len(s)):
            if ((s[j][0]<=f[i][0] and f[i][0]<=s[j][1]) or (s[j][0]<=f[i][1] and f[i][1]<=s[j][1]) or (s[j][0]>=f[i][0] and f[i][1]>=s[j][0])):
                ans.append([max(s[j][0],f[i][0]),min(f[i][1],s[j][1])])
            if(s[j][1]<f[i][1]):
                j+=1
            else:
                i+=1
        return ans