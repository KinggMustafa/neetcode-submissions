# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]
            v1, left = dfs(root.left)
            v2, right = dfs(root.right)
            verdict = abs(left - right) <= 1 and v1 and v2
            return [verdict, 1 + max(left, right)]

        return dfs(root)[0]
        #best case: time complexity o(logn) (height of the tree), worst case o(n)