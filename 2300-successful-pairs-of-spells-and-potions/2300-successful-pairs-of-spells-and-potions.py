class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], su: int) -> List[int]:
        ans=[]
        potions.sort()
        for i in range(len(spells)):
            l=0
            r=len(potions)
            while(l<r):
                mid=(l+r)//2
                if(spells[i]*potions[mid]<su):
                    l=mid+1
                else:
                    r=mid
            ans.append(len(potions)-l)
        return ans
        