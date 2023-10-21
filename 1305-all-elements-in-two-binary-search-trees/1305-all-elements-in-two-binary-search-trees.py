# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:       
        
        def helper1(root1):
            
            list1=[]
            
            if not root1:
                
                return []
            
            stack1=[]
            stack1.append(root1)
            
            while stack1:
                
                node=stack1.pop()
                
                list1.append(node.val)
                
                if node.right:
                    stack1.append(node.right)
                    
                if node.left:
                    stack1.append(node.left)
                    
            return list1
        
        
        def helper2(root2):
            
            list2=[]
            
            if not root2:
                return []
            
            stack2=[]
            stack2.append(root2)
            
            while stack2:
                node=stack2.pop()
                
                list2.append(node.val)
                
                if node.right:
                    stack2.append(node.right)
                    
                if node.left:
                    stack2.append(node.left)
                    
            return list2 
        
        print(helper1(root1)) 
        res=sorted(helper1(root1)+helper2(root2))
        
        return res
        
    