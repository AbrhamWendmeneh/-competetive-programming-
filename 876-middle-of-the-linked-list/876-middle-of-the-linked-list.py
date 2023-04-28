# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        current=slow
        result=[]
        while current:
            result.append(current.val)
            current=current.next
        if not result:
            return None
        head=ListNode(result[0])
        node=head
        for i in result[1:]:
            node.next=ListNode(i)
            node=node.next
        return head