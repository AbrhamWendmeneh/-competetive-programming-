# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        new_list=[]
        node=head
        
        while node:
            
            new_list.append(node.val)
            node=node.next
            
        result=0
        
        for i in range(len(new_list)):
            
            val=new_list[i]+new_list[len(new_list)-i-1]
            result=max(result,val)
            
        return result