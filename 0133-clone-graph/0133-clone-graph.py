"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        visited={}
        def dfs(test):
            if test in visited:
                return visited[test]
            current=Node(test.val)
  
            visited[test]=current
            
            for i in test.neighbors:
                clone_neigh= dfs(i)
                current.neighbors.append(clone_neigh)
            return current
        return dfs(node)
        