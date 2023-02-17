# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        a=head
        b=None
        while a!=None:
            if a.val==val and b==None:
                a=a.next
                head=a
                b=None
            elif a.val==val:
                b.next=a.next
                a=a.next
            else:
                b=a
                a=a.next
        return head
    
    
                
                
                
                
        