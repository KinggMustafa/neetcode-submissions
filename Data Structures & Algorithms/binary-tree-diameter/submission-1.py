# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            height = max(1 + left, 1 + right)
            diameter = left + right
            self.res = max(self.res, diameter)
            return height
        dfs(root)
        return self.res
        #O(n) time where n is the length of all nodes, o(h) space where h is the height of the recursion stack