# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        elif not list2:
            return list1
        
        elif list1.val < list2.val:
            res=ListNode(list1.val)
            list1=list1.next
        else:
            res=ListNode(list2.val)
            list2=list2.next
        
        return ListNode(res.val,self.mergeTwoLists(list1,list2))