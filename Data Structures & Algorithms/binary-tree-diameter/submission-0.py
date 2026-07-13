# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = 0
        right = 0
        if root.left:
            left = 1 + self.depth(root.left)
        if root.right:
            right = 1 + self.depth(root.right)
        self.result = max(self.result, left + right)
        #we need to return result for our final answer but for each left and right call we need to return the depth of that particular node
        return max(left,right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        self.result = 0
        self.depth(root)
        return self.result
    #o(n) time with o(h) height of the tree