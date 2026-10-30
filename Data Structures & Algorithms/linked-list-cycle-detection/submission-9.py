# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev = head
        fast = head
        while prev and fast and fast.next:
            prev = prev.next
            fast = fast.next.next
            if prev == fast:
                return True
        return False