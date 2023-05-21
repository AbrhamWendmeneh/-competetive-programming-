# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        new_list=[]
        node=head
        while node:
            new_list.append(node.val)
            node=node.next
            
        index=len(new_list)//2
        array=new_list[:index]+new_list[index+1:]
        val=ListNode(array[0])
        curr=val
        for i in range(1,len(array)):
            
            curr.next=ListNode(array[i])
            curr=curr.next
            
        return val
        
            