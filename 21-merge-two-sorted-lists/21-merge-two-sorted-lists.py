# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        con_list=ListNode
        head=con_list
        while (list1 and list2):
            if list1.val< list2.val:
                con_list.next=list1
                list1=list1.next
            else:
                con_list.next=list2
                list2=list2.next
            con_list=con_list.next
        con_list.next = list1 or list2
        return head.next
                