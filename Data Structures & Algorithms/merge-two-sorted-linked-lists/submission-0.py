# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 = list1
        curr_2 = list2
        head = None
        curr = head
        while (curr_1 != None and curr_2 != None):
            if curr_1.val <= curr_2.val:
                if head == None:
                    head = ListNode(curr_1.val, None)
                    curr = head
                else:
                    curr.next = ListNode(curr_1.val, None)
                    curr = curr.next
                curr_1 = curr_1.next
            else:
                if head == None:
                    head = ListNode(curr_2.val, None)
                    curr = head
                else:
                    curr.next = ListNode(curr_2.val, None)
                    curr = curr.next
                curr_2 = curr_2.next
        while (curr_1 != None):
            if head == None:
                head = ListNode(curr_1.val, None)
                curr = head
            else:
                curr.next = ListNode(curr_1.val, None)
                curr = curr.next
            curr_1 = curr_1.next
        while (curr_2 != None):
            if head == None:
                head = ListNode(curr_2.val, None)
                curr = head
            else:
                curr.next = ListNode(curr_2.val, None)
                curr = curr.next
            curr_2 = curr_2.next
        return head