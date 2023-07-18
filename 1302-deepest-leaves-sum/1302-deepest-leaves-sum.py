# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            left=depth(node.left)
            right=depth(node.right)
            return max(left,right)+1
        def traverseSum(node):
            queue=deque([(node, 0)])  
            max_depth=depth(node)
            
            res=0
            
            while queue:
                curr_node,dist=queue.popleft()
                if dist== max_depth-1:
                    res +=curr_node.val
                else:
                    
                    for i in [curr_node.left,curr_node.right]:
                        if i:              
                            queue.append((i,dist+1))
            return res
        return traverseSum(root)
    
    '''
    time complexity of this code is O(N), where N is the number of nodes in the binary tree.
    
     space complexity is O(M), where M is the maximum number of nodes at any level in the binary tree.
     
     I have do this question based on the hint given in the question which makes easy for me to write the implementation of it 
     
     in the first function (depth(node)) I write code that returns value for the maximum depth of the tree 
     and based on the value it I create another function which is called treaverseSum in which this function uses the idea of BFS to traverse through the tree and if it gets the value of dist equal to the value from the depth function it adds all of the values from it to sum up and finally return the final answer.
    
    '''
