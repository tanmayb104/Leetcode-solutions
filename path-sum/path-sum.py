# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if(not root):
            return False
        
        su=[]
        st=[[root,1]]
        while(st):
            a,d=st.pop()
            su=su[:d-1]
            su.append(a.val)
            # print(su,st)
            if(not a.left and not a.right):
                if(sum(su[:d])==targetSum):
                    return True
                else:
                    su.pop()
            if(a.left):
                st.append([a.left,d+1])
            if(a.right):
                st.append([a.right,d+1])
        return False
            
        