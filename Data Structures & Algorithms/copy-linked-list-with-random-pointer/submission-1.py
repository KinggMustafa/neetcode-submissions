"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodemap = {}
        #we create a node map, key is the original, and value is the copy node.
        curr = head
        while curr:
            nodemap[curr] = Node(curr.val, None, None) #the copy node will have no next or random pointer until our second loop where we can access any copy value
            curr = curr.next
        traverse = head
        while traverse:
            nodemap[traverse].next = nodemap.get(traverse.next, None)
            nodemap[traverse].random = nodemap.get(traverse.random, None)
            traverse = traverse.next
        return nodemap.get(head)
        #time complexity: o(n), space is o(n) where n is the length of our original set of nodes