# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        found_nodes = set()
        curr = head
        while (curr != None):
            if curr in found_nodes:
                return True
            found_nodes.add(curr)
            curr = curr.next

        return False




