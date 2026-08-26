# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isvalid(low, high, root):
            if not root:
                return True
            if not (low < root.val < high):
                return False
            left = isvalid(low, root.val, root.left)
            right = isvalid(root.val, high, root.right)
            return left and right            
        low = float('-INF')
        high = float('INF')
        return isvalid(low, high, root)
#o(n) time bc we visit every node once, height is o(h) height of the tree


