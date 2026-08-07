# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def addup(node):
            arr.append(node.val)
            if node.left:
                addup(node.left)
            if node.right:
                addup(node.right)
        addup(root)
        arr = sorted(arr) #nlogn time
        
        for i in range(len(arr)):
            if (i + 1) == k:
                return arr[i]
        #o(nlogn) time, space is o(n)
        
        