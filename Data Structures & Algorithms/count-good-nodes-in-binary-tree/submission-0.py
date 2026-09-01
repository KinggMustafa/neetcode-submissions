# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maximum = float('-INF')
        self.res = 0
        def count(maximum, root):
            if root.val >= maximum:
                self.res += 1
                maximum = root.val
            if root.left:
                count(maximum, root.left)
            if root.right:
                count(maximum, root.right)
        count(maximum, root)
        return self.res
        #O(n) time and o(h) space