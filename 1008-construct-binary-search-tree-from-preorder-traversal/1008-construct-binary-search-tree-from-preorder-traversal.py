# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None
        
        else:
            
            root=TreeNode(preorder[0])
            
            for i in range(1,len(preorder)):
                
                root_val=root
                val=preorder[i]
                while True:
                    
                    #If the current element is less than the node value, 
                    #add it as the left child of the node.
                    
                    if val < root_val.val:
                        
                        if not root_val.left:
                            
                            root_val.left=TreeNode(val)
                            
                            break
                            
                        else:
                            
                            root_val=root_val.left
                            
                    #If the current element is greater than the node value, 
                    #add it as the right child of the node.
                    
                    elif val>root_val.val:
                        
                        if not root_val.right:
                            
                            root_val.right=TreeNode(val)
                            
                            break
                            
                        else:
                            
                            root_val=root_val.right
                            
                    #If the current element is between the node value and its parent value, 
                    #set the current element as the right child of the parent node.  
                    
                    else:
                        
                        if not root_val.right:
                            
                            root_val.right=TreeNode(val)
                            
                            break
                            
                        else:
                            
                            root_val=root_val.right
                            
        return root
    
    
