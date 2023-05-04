# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        setval=set()
        
        # Define a recursive helper function that 
        #takes in the preorder and inorder lists
        def helper(preorder,inorder):
            
            # If the inorder list is empty, return None
            if not inorder:
                return None
            
            # Pop the first element from the preorder list 
            #to get the root value
            rootval=preorder.pop(0)
            
            root=TreeNode(rootval)
            
            rootindex=inorder.index(rootval)
            
                        
            # If the root value has not been visited before,
            # add it to the setval set
            # and construct the left and right subtrees recursively
            
            if rootval not in setval:
                
                setval.add(rootval)
                
                root.left=helper(preorder,inorder[:rootindex])
                
                root.right=helper(preorder,inorder[rootindex+1:])
                
            # else:
            #     return None
                
            return root
        
        return helper(preorder,inorder)
            
            
            
            
            
            
        
        