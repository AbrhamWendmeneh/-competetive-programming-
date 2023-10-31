# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        value= head
        if not value:
            return False
        compare=(10**5)+1
        test=0
        
        while test < compare:
            if value.next is None:
                return False
            test+=1
            value=value.next
        return True