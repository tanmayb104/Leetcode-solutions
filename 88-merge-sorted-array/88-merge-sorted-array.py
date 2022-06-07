class Solution:
    def merge(self, n1: List[int], m: int, n2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num=[]
        i=0
        j=0
        while(i<m and j<n):
            if(n1[i]<n2[j]):
                num.append(n1[i])
                i+=1
            else:
                num.append(n2[j])
                j+=1
        while(i<m):
            num.append(n1[i])
            i+=1
        while(j<n):
            num.append(n2[j])
            j+=1
        for i in range(len(num)):
            n1[i]=num[i]
        print(n1)