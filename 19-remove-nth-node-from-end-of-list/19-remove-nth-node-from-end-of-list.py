# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # value=head
        # result=[]
        # count=0
        # while value and value.next:
        #     if count==n:
        #         value=value.next.next
        #         count+=1
        #     result.append(value.val)
        #     value=value.next
        #     count+=1
        # head=ListNode(result[0])
        # node=head
        # for i in result[1:]:
        #     node.next=ListNode(i)
        #     node=node.next
        # return head
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        index = length - n

        if index == 0:
            return head.next
        
        node = head
        for i in range(index - 1):
            node = node.next
    
        node.next = node.next.next
        
        return head