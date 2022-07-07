class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache()
        def rec(i,j,k):
            if(i==len(s1) and j==len(s2) and k==len(s3)):
                return True
            elif(i==len(s1)):
                if(s2[j]==s3[k]):
                    return rec(i,j+1,k+1)
                return False
            elif(j==len(s2)):
                if(s1[i]==s3[k]):
                    return rec(i+1,j,k+1)
                return False
            
            if(s1[i]==s2[j] and s2[j]==s3[k]):
                return rec(i+1,j,k+1) or rec(i,j+1,k+1)
            elif(s1[i]==s3[k]):
                return rec(i+1,j,k+1)
            elif(s2[j]==s3[k]):
                return rec(i,j+1,k+1)
            return False
        
        if(len(s1)+len(s2)!=len(s3)):
            return False
        return rec(0,0,0)