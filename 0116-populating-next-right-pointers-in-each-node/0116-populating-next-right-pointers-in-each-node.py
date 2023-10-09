"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        queue=[]
        queue.append(root)
        while len(queue):
            val=len(queue)
            res=[]
            while val >0:
                node=queue.pop(0)
                res.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if node is None:
                    continue
                val-=1
            for i in range(len(res)-1):
                res[i].next=res[i+1]
        return root
                
                
                
        