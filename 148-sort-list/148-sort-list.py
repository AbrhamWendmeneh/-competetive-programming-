# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        # split the list into two halves
        prev = None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None  
        
        # recursively sort the two halves
        left = self.sortList(head)
        right = self.sortList(slow)
        
        # merge the sorted halves
        return self.merge(left, right)
    
    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        if left is None:
            return right
        if right is None:
            return left
        
        dummy = ListNode()  # dummy node for the merged list
        current = dummy
        
        while left is not None and right is not None:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        
        # append the remaining nodes
        if left is not None:
            current.next = left
        if right is not None:
            current.next = right
        
        return dummy.next
                