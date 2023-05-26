# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1=''
        num1=l1
        while num1:
            val1 += str(num1.val)
            num1 =num1.next
            
        val2=''
        num2=l2
        while num2:
            val2 +=str(num2.val)
            num2 = num2.next
            
        sumval= str(int(val1) + int(val2))
        
        node=ListNode(int(sumval[0]))
        current=node
        
        for i in range(1,len(sumval)):
            
            current.next=ListNode(int(sumval[i]))
            current=current.next
            
        return node
    
            