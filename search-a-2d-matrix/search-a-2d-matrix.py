class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        while(top<=bottom):
            mid=(top+bottom)//2
            if(matrix[mid][left]<=target<=matrix[mid][right]):
                top=mid
                break
            elif(target<matrix[mid][left]):
                bottom=mid-1
            else:
                top=mid+1
        row=top
        if(row>=len(matrix) or row<0):
            return False
        while(left<=right):
            mid=(left+right)//2
            if(matrix[row][mid]==target):
                return True
            elif(matrix[row][mid]<target):
                left=mid+1
            else:
                right=mid-1
        return False
        