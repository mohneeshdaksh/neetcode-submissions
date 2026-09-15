# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while True:
            if head is None:
                return False
            if head not in seen:
                seen.add(head)
                head = head.next
                continue
            else:
                return True