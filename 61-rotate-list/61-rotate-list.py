# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        node=head
        nums=[]
        while node:
            nums.append(node.val)
            node=node.next
                
        k=k%(len(nums))
        
        nums[:]=nums[-k:]+nums[:-k]
        nums1=nums
        
        val=ListNode(nums1[0])
        current=val
        for i in range(1,len(nums1)):
            current.next=ListNode(nums1[i])
            current=current.next
        return val
            
            