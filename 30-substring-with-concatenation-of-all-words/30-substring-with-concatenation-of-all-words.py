class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        c1=Counter(words)
        so=''.join(sorted("".join(words)))
        ans=[]
        # print(so)
        for i in range(len(s)-len(so)+1):
            a=''.join(sorted(s[i:i+len(so)]))
            # print(a)
            if(a==so):
                l=[]
                for j in range(i,i+len(so),len(words[0])):
                    l.append(s[j:j+len(words[0])])
                # print(l)
                c2=Counter(l)
                if(c1==c2):
                    ans.append(i)
        return ans