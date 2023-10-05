# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
             
        def helper(postorder, inorder):
            if not inorder:
                return None
            
            # Pop the first element from the preorder list 
            rootVal= postorder.pop()
            
            root= TreeNode(rootVal)
            
            rootIndex= inorder.index(rootVal)
                   
            root.right=helper(postorder,inorder[rootIndex+1:])
            
            root.left=helper(postorder,inorder[:rootIndex])
            
            return root
        
        
        return helper(postorder,inorder)
    
    '''
    I have done this question by getting an intution from the question number
    105 which says about consturcting binary tree from inorder and preorder            traversal with some little change from it.
   
    '''
        