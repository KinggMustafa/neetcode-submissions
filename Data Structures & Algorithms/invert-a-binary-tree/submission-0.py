# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        lft = root.left
        rght = root.right
        root.left = rght
        root.right = lft
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root
    #o(n) time where n is the number of nodes we visit