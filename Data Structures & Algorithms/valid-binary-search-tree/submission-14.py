# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isvalid(lower, upper, root):
            if not lower < root.val < upper:
                return False
            left, right = True, True
            if root.left:
                left = isvalid(lower, root.val, root.left) 
            if root.right:
                right = isvalid(root.val, upper, root.right)
            return left and right

        lower, upper = float('-INF'), float('INF')
        return isvalid(lower, upper, root)
        #o(n) time and o(h) space
        #if we do not do if root.left, at every leaf node we do 2 redundant calls which give us n+1 more redundant calls so the time would have still been 2n or o(n) but this saves more time