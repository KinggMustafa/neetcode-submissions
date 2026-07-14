# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]
            vleft, hleft = dfs(node.left)
            vright, hright = dfs(node.right)
            verdict = vleft and vright and (abs(hleft - hright) <= 1)
            return [verdict, 1 + max(hleft, hright)]
    
        return dfs(root)[0]
        #o(n) time with o(h) space -> height of the tree
        