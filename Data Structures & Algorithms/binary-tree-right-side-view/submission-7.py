# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        queue = deque([root])
        res = []

        if not root:
            return res
        while queue:
            length = len(queue)
            right = None
            for i in range(length):
                right = queue.popleft()
                if right.left:
                    queue.append(right.left)
                if right.right:
                    queue.append(right.right)
            res.append(right.val)
        return res
        #o(n) time bc we visit every node, o(n) space