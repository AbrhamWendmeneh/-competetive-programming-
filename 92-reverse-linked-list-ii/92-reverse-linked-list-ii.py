# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right==left:
            return head
        newlist=[]
        node=head
        while node:
            newlist.append(node.val)
            node=node.next
        array= newlist[:left-1]+newlist[left-1:right][::-1]+newlist[right:]
        
        node=ListNode(array[0])
        current=node
        
        for i in range(1,len(array)):
            current.next=ListNode(array[i])
            current=current.next
        return node