# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #first I convert the linked list to array as follows
        node=head
        new_list=[]
        
        while node:
            
            new_list.append(node.val)
            
            node=node.next
            
        #I swap the values of the given postion in the linked list using the array 
        new_list[k-1],new_list[-k]=new_list[-k],new_list[k-1]
        
        #I construct the linked list from the new array 
        
        val=ListNode(new_list[0])
        curr=val
        
        for i in range(1,len(new_list)):
            
            curr.next=ListNode(new_list[i])
            
            curr=curr.next
            
        return val
