# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node=head
        new_list=[]
        
        while node:
            
            new_list.append(node.val)
            node = node.next

        for i in range(1, len(new_list), 2):
            new_list[i], new_list[i-1] = new_list[i-1], new_list[i]
            
        # Dummy node to simplify the list creation
        new_head = ListNode(0)  
        curr = new_head
        
        for val in new_list:
            
            curr.next = ListNode(val)
            curr = curr.next
        
        return new_head.next
