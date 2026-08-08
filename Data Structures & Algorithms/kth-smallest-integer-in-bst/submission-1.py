# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 1
        self.res = None
        def iterate(node):
            if not node:
                return 
            if node.left:
                iterate(node.left)
            if self.count == k:
                self.res = node.val
                self.count += 1
                return
            else:
                self.count += 1
                iterate(node.right)
        iterate(root)
        return self.res
        #o(n) time bc we visit ever node once until we find our result so worst case is o(n), space is o(h), height of the tree best logn worst n
