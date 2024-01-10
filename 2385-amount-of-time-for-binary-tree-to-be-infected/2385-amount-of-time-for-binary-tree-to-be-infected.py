# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        graph = {}
        
        def helper(node):
            
            if node:
                if node.left:
                    if node.val in graph:
                        
                        graph[node.val].append(node.left.val)
                        
                    else:
                        graph[node.val] = [node.left.val]
                        
                    if node.left.val in graph:
                        
                        graph[node.left.val].append(node.val)
                        
                    else:
                        
                        graph[node.left.val]= [node.val]
                        
                if node.right:
                    
                    if node.val in graph:
                        
                        graph[node.val].append(node.right.val)
                        
                    else:
                        
                        graph[node.val] = [node.right.val]
                    
                    if node.right.val in graph:
                        
                        graph[node.right.val].append(node.val)
                        
                    else:
                        
                        graph[node.right.val] = [node.val]
                        
                helper(node.left)
                helper(node.right)
                
        helper(root)
        print(len(graph))
        
        if len(graph) < 1:
            
            return 0
        
        print(graph)
        
        answer = 0
        queue =  deque([start])
        visited = set()
        visited.add(start)
        
        while queue:
   
            for i in range(len(queue)):
        
                node = queue.popleft()
                             
                for val in graph[node]:
                    
                    if val not in visited:
                        
                        visited.add(val)
                        
                        queue.append(val)
            answer += 1
            
        return answer - 1
    
    
'''
        
{1:[3,5] , 3:[10,6] , 5:[4], 4:[9,2]}
 {3:[10,6], 1:[3,5], 5:[4], 4:[9,2]}
 {
  3:[1,10,6], 1 
  10:[3], 2
  6:[3], 2
  1:[3,5],  2
  5:[1,4], 3 
  4:[9,2],  4
  9:[4], 
  2:[4]
  }

'''


        
        
                        
                
            
                        
                
                    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            