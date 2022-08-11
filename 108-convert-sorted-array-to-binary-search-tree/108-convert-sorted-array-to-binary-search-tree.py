# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l=0
        r=len(nums)-1
        
        def rec(l,r):
            if(l<=r):
                mid=(l+r)//2
                node=TreeNode(nums[mid])
                node.left=rec(l,mid-1)
                node.right=rec(mid+1,r)
                return node
        return rec(l,r)