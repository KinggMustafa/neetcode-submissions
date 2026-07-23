# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        if not root:
            return []
        q.append(root)

        while q:
            sublist = []
            length = len(q)
            for i in range(length):
                val = q.popleft()
                if val.left:
                    q.append(val.left)
                if val.right:
                    q.append(val.right)
                sublist.append(val.val)
            res.append(sublist)
        return res
    #o(n) time because we visit every node once, o(1) space


            
