# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        dummy = ListNode(0,head) #dummy node points to the head at first, we save a dummy node to returnn the head
        traverse = head
        position = 0
        prev = dummy
        while traverse:
            position += 1
            if position == ((length - n)+1):
                prev.next = prev.next.next
                break
            else:
                prev = traverse
                traverse = traverse.next
        return dummy.next

                
