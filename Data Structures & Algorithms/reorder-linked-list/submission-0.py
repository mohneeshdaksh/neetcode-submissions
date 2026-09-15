# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        second_head = self.find_mid_and_split(head)
        reversed_second_head = self.reverse_second_half(second_head)
        curr = head
        while reversed_second_head:
            nxt = curr.next
            second_half_next = reversed_second_head.next
            curr.next = reversed_second_head
            reversed_second_head.next = nxt
            curr = nxt
            reversed_second_head = second_half_next
    
    def find_mid_and_split(self, head: Optional[ListNode]):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_head = slow.next
        slow.next = None
        return second_head
    
    def reverse_second_half(self, head: Optional[ListNode]):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev