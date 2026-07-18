# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, subroot):
            if not root and not subroot:
                return True
            if not root and subroot:
                return False
            if root and not subroot:
                return False
            if root.val != subroot.val:
                return False
            left = dfs(root.left, subroot.left)
            right = dfs(root.right, subroot.right)
            verdict = (left and right)
            return verdict

        #we need to call isSubtree on every node
        if not root:
            return False
        if dfs(root, subRoot):
            return True
        if self.isSubtree(root.left, subRoot):
            return True
        if self.isSubtree(root.right, subRoot):
            return True
        return False
        #o(n times m) where n is root and m is subroot
        #o(h) space where h is the height of the tree. worst case o(n) best case logn (balanced tree)        
        



