# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Reverse the linked list
        prev = None
        curr = head
        _next = head.next
        while curr != None:
            curr.next = prev
            prev = curr
            curr = _next
            if _next:
                _next = _next.next
        head = prev
        # Then loop through, counting up until reached the nth element and remove
        i = 1
        prev = None
        curr = head
        while (i < n):
            print(i, n)
            prev = curr
            curr = curr.next
            i += 1
        if prev:
            prev.next = curr.next
        else:
            head = head.next
        # Reverse the linked list
        prev = None
        curr = head
        _next = head.next if head else None
        while curr != None:
            curr.next = prev
            prev = curr
            curr = _next
            if _next:
                _next = _next.next
        head = prev
        return head
        
        