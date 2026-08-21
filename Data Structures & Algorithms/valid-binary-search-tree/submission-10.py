# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isvalid(root, lower, upper):
            if not root:
                return True
            left, right = True, True

            if not ( lower < root.val < upper ):
                return False
            if root.left:
                if root.left.val >= root.val:
                    return False
                left = isvalid(root.left, lower, root.val)
            
            if root.right:
                if root.right.val <= root.val:
                    return False
                right = isvalid(root.right, root.val, upper)
                
            return left and right
            
        
        lower, upper = float('-INF'), float('INF')
        return isvalid(root, lower, upper)