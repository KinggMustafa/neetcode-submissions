# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        res = []
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
        #o(n) time bc we visit each node, o(n) space bc we store up to n nodes
                           

                