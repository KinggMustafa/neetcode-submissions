# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isvalid(lower, upper, root):
            if not root:
                return True
            if not lower < root.val < upper:
                return False
            left = isvalid(lower, root.val, root.left)
            right = isvalid(root.val, upper, root.right)
            return left and right

        lower, upper = float('-INF'), float('INF')
        return isvalid(lower, upper, root)
        #o(n) time and o(h) space