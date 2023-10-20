"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []
        
        queue=deque()
        queue.append(root)
        list_val=[]
        
        while queue:          
            
            level=[]
            size=len(queue)
            
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.children:
                    for child in node.children:
                        queue.append(child)
                    
            list_val.append(level)
            
        return list_val
        