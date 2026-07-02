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
        #then go through the original nodes again, and apply the next and random values to our copy nodes

        nodemap = {}
        curr = head
        while curr:
            nodemap[curr] = Node(curr.val)
            curr = curr.next
                #create a hashmap: {key = original node, value equals copy node}

        traverse = head
        while traverse:
            nxt = traverse.next
            ran = traverse.random
            nodemap[traverse].next = nodemap.get(nxt, None)
            nodemap[traverse].random = nodemap.get(ran, None)
            traverse = traverse.next
        return nodemap.get(head, None)
    #o(n) time where n is the length of nodes, o(n) space where n is the length of nodes (that are copied)
    #key error for indexing into a hashmap only happens for reads, not writing. 
        
