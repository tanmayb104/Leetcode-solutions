class Solution:
    def maxArea(self, h: int, w: int, ho: List[int], ve: List[int]) -> int:
        ho.sort()
        ve.sort()
        ho=[0]+ho+[h]
        ve=[0]+ve+[w]
        ph=0
        for i in range(1,len(ho)):
            ph=max(ph,ho[i]-ho[i-1])
        pv=0
        for i in range(1,len(ve)):
            pv=max(pv,ve[i]-ve[i-1])
        return (ph*pv)%(10**9+7)