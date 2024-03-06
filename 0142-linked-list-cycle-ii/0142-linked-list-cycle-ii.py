# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        value = head 
        
        if not value:
            
            return None
        
        set_val = set()
        
        while value:
            
            if value in set_val:
                
                return value
            
            set_val.add(value)
            
            value = value.next
              
        return None
            
            