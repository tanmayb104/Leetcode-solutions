# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def calc(node,d):
    if(node.left and node.right):
        d[node]=[0,0]
        d[node][0]=calc(node.left,d)+1
        d[node][1]=calc(node.right,d)+1
    elif(node.left):
        d[node]=[0,0]
        d[node][0]=calc(node.left,d)+1
    elif(node.right):
        d[node]=[0,0]
        d[node][1]=calc(node.right,d)+1
    else:
        return 0
    return max(d[node][0],d[node][1])
    
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d={}
        calc(root,d)
        m=0
        for i in d.values():
            m=max(i[0]+i[1],m)
        return m