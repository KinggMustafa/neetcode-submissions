# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        best = 1

        if root.left:
            best = max(best, 1 + self.maxDepth(root.left))
        if root.right:
            best = max(best, 1 + self.maxDepth(root.right))
        return best
        #o(n) time
        #o(logn) space (best case) because our node calls are leveled, worst case space is o(n) if all our nodes are called at once