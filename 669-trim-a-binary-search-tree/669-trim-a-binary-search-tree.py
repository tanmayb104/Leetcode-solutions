# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        while((low>root.val and root.right) or (root.val>high and root.left)):
            if(low>root.val):
                root=root.right
            else:
                root=root.left
        if(root.val>high or root.val<low):
            return None
        head=root
        par=root
        if(root.left):
            root=root.left
            while(root):
                if(low<=root.val and root.left):
                    par=root
                    root=root.left
                elif(low>root.val):
                    par.left=root.right
                    root=root.right
                else:
                    break
                # print(head)
        root=head
        par=root
        if(root.right):
            root=root.right
            while(root):
                # print(root)
                if(high>=root.val and root.right):
                    par=root
                    root=root.right
                elif(high<root.val):
                    par.right=root.left
                    root=root.left
                else:
                    break
        return head