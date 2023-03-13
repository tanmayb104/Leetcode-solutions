# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if(not root or (not root.left and not root.right)):
            return True
        elif(not root.left or not root.right):
            return False
        bfs1=deque([-1,root.left])
        bfs2=deque([-1,root.right])
        while(bfs1 and bfs2):
            a1=bfs1.popleft()
            a2=bfs2.popleft()
            if(a1==-1 and a2==-1):
                if(len(bfs1) and len(bfs2)):
                    bfs1.append(-1)
                    bfs2.append(-1)
            elif(a1.val==a2.val):
                # print(a1.val,a2.val)
                if(a1.left and a2.right):
                    bfs1.append(a1.left)
                    bfs2.append(a2.right)
                elif(not a1.left and not a2.right):
                    pass
                else:
                    return False
                if(a1.right and a2.left):
                    bfs1.append(a1.right)
                    bfs2.append(a2.left)
                elif(not a1.right and not a2.left):
                    pass
                else:
                    return False
            else:
                return False
        return True
            
        