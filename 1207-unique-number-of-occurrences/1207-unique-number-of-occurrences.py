class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c=Counter(arr)
        s=set()
        for i in c:
            s.add(c[i])
        return len(s)==len(c)