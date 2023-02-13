# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i=head
        '''       while i and i.next:
            if i.val == i.next.val:
                i.next=i.next.next
            else:
                i=i.next
        
       
        return head'''
        while i:
            while i.next and i.next.val==i.val:
                i.next=i.next.next
            i=i.next
        return head