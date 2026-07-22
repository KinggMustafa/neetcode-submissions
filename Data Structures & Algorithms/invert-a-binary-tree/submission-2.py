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
        self.invertTree(lft)
        self.invertTree(rght)
        return root
        #o(n) time and o(h) height