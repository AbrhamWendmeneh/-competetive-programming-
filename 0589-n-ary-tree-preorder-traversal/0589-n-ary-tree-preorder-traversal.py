"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root:
            
            return []
        
        stack=[root]
        result=[]
        
        while stack:
                    
            node=stack.pop()
            result.append(node.val) 
            
            if node.children:
                
                #this is the basic thing in this code 
                #that I have used to get the leftmost value
                
                for child in (node.children)[::-1]:   
                    
                    stack.append(child)
                    
        return result
        
        