# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque 
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        '''
        The first thing I want to do is finding the targeted value from the list of nodes using DFS and then find values from the distance k
        '''
        # DFS
        par_map={}
        stack=[root]
        
        while stack:
            
            node=stack.pop()
            if node.left:
                stack.append(node.left)
                par_map[node.left.val]=node
                
            if node.right:
                stack.append(node.right)
                par_map[node.right.val]=node
                
            if node.val ==target.val:
                break
                
        # BFS 
        result=[]
        queue=deque([(node, 0)])
        visited=set([node])
        
        while queue:
            curr_node,dist= queue.popleft()
            
            if dist == k:
                result.append(curr_node.val)
            elif dist < k:
                for i in [curr_node.left,curr_node.right, par_map.get(curr_node.val)]:
                    
                    if i and i not in visited:
                        visited.add(i)
                        queue.append((i,dist+1))
                        
        return result
            