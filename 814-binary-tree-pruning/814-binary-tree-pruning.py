class Solution(object):
    def pruneTree(self, root):
        if root==None:
            return None
        _l = self.pruneTree(root.left)
        _r = self.pruneTree(root.right)
        if root.val == 0 and _l == None and _r == None:
            return None
        else:
            root.left = _l
            root.right = _r
        return root