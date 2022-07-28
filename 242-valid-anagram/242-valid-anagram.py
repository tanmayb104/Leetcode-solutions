from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1=Counter(s)
        c2=Counter(t)
        try:
            if(c1.keys()==c2.keys()):
                for i in c1.keys():
                    if(c1[i]!=c2[i]):
                        return False
                return True
        except:
            return False