# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #first we have to know the length of our lsit
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        #we want to cut the array at n//2
        curr = head
        position = 0
        while curr:
            position += 1
            if position == (length //2)+1:
                newhead = curr.next
                curr.next = None
            curr = curr.next

        #reverse the second half of the list
        prev = None
        while newhead:
            nxt = newhead.next
            newhead.next = prev
            prev = newhead
            newhead = nxt
        

        while head and prev:
            nxtnode = head.next
            nxtadd = prev.next
            head.next = prev
            prev.next = nxtnode
            head = nxtnode
            prev = nxtadd
        
        
        

            