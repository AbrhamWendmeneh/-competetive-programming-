# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        levels = []
        queue = deque([root])
        
        while queue:
            
            level_size = len(queue)
            current_level = []
            
            for i in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            levels.append(current_level)
            
        total_swaps = 0
        
        for level in levels:
            
            sorted_level = sorted(level)
            
            value_to_sorted_map = {val: idx for idx, val in enumerate(sorted_level)}
            visited = [False] * len(level)
            
            swaps = 0 
            
            for i in range(len(level)):
                
                if visited[i] or level[i] == sorted_level[i]:
                    continue
                
                cycle_size = 0
                current = i
                
                while not visited[current]:
                    visited[current] = True
                    next_index = value_to_sorted_map[level[current]]
                    current = next_index
                    cycle_size += 1
                    
                if cycle_size > 1:
                    swaps += cycle_size  - 1
                    
            total_swaps += swaps 
            
        return total_swaps
        
            
            
        