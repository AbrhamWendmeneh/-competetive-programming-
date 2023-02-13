# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        first = 0
		
		
        while l1:
            first = l1.val * pow(10, i) + first
            l1 = l1.next
            i += 1
        
		
        i = 0
        second = 0
        while l2:
            second = l2.val * pow(10, i) + second
            l2 = l2.next
            i += 1
        
		
        total = first + second
		
        
        head = ListNode(total%10)
        total = total//10
        temp = head
        
        while(total > 0):
            node = ListNode(total%10)
            total = total//10
            temp.next = node
            temp = temp.next
        
		
        return head
        