# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for head in lists:
            while head:
                heapq.heappush(heap, head.val)
                head = head.next
        dummy = ListNode(-1)
        curr = dummy

        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next

        return dummy.next
