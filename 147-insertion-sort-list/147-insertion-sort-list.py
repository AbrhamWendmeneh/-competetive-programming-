# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # for i in range(len(head)):
        #     if self.val= head[i]:
        '''this method is using list inorder to store the value of linked list for future use'''
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        lst = sorted(lst)
        acc = ListNode(0)
        temp = acc
        for i in lst:
            temp.next = ListNode(i)
            temp = temp.next
        return acc.next
                
        