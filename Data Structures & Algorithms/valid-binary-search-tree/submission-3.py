# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validator(lower, upper, node):
            if not node:
                return True
            if node.val <= lower:
                return False
            if node.val >= upper:
                return False
            cond1, cond2 = True, True
            if node.left:
                cond1 = validator(lower, node.val, node.left)
            if node.right:
                cond2 = validator(node.val, upper, node.right)
            
            return cond1 and cond2 
        
        lower = float('-INF')
        upper = float('INF')
        if not validator(lower, upper, root):
            return False
        return validator(lower, root.val, root.left) and validator(root.val, upper, root.right)




