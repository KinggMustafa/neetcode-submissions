# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def depth(self, root: Optional[TreeNode]) -> bool:
        res = 1
        if not root:
            return 0
        if root.left:
            res = max(res, 1 + self.depth(root.left))
        if root.right:
            res = max(res, 1 + self.depth(root.right))
        return res


    def diameter(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        return abs(left - right)



    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #diameter of the left + right and if its less than 1 its balanced
        if not root:
            return True
        if self.diameter(root) > 1:
            return False
        if root.left:
            if not self.isBalanced(root.left):
                return False
        if root.right:
            if not self.isBalanced(root.right):
                return False
        
        return True
        