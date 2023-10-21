"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        level=0
        
        if not root:
            return level
        
        queue=deque([root])
        
        while queue:
            
            size= len(queue)
            level+=1
            
            for _ in range(size):
                node=queue.popleft()
                
                if node.children:
                    for child in node.children:
                        queue.append(child)
        return level
        
        