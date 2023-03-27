# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None:
            return None
        
        
        #for this case We have to find the left values of the tree in           our tree in which our root value is greater than the target             value that we intend to find so that we stop to investigate the         right part 
        
        if root.val > val:
            return self.searchBST(root.left,val)
        
        
        #the same is true for this case in which we stop finding values         in the right direction according to root val of the currect val         then 
        
        if root.val < val:
            return self.searchBST(root.right,val)
        
        
        
        #the thing that we have asked is that to return the values form          the target one to root value then we simply returns it as root          it exists otherwise return None as result
        
        return root
                
            