from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c=Counter(s1)
        l=0
        r=0
        while(r<len(s2)):
            if(s2[r] in c and c[s2[r]]):
                c[s2[r]]-=1
                r+=1
            elif(s2[r] in c):
                if(r-l==len(s1)):
                    return True
                else:
                    while(s2[l]!=s2[r]):
                        c[s2[l]]+=1
                        l+=1
                    l+=1
                    r+=1
            else:
                if(r-l==len(s1)):
                    return True
                else:
                    r+=1
                    while(l<r and l<len(s2)):
                        if(s2[l] in c):
                            c[s2[l]]+=1
                        l+=1
        if(r-l==len(s1)):
            return True
                
        return False
                        
                
                
        