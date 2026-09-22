# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Hackish way first, convert linked list into a list
        # and then reorder that one
        list_version = []
        while (head != None):
            list_version.append(head)
            head = head.next
        size = len(list_version)
        count = 1
        original_list = list_version.copy()
        for i in range(1, size):
            if i % 2:
                list_version[i] = original_list[size - count]
            else:
                list_version[i] = original_list[count]
                count += 1
        # Convert back into linked list
        head = list_version[0]
        for i in range(1, size):
            head.next = list_version[i]
            head = head.next
        head.next = None
