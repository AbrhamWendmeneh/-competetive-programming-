# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        new_list1=[]
        node=head
        
        while node:
            new_list1.append(node.val)
            node=node.next
        result=[]
        max_val= new_list1[-1]
        
        for i in reversed(new_list1):
            if max_val <= i:
                result.append(i)
                max_val= i
                
        node=ListNode(0)
        current = node
        
        for i in reversed(result):
            current.next=ListNode(i)
            current=current.next
            
        return node.next
            
        