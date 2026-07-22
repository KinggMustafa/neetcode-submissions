# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if not root:
            return 0
        depth = max(depth, 1 + self.maxDepth(root.left))
        depth = max(depth, 1 + self.maxDepth(root.right))
        return depth 
        #o(n) where n is the number of nodes in the tree