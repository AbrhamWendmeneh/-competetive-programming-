# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.indx=-1
        self.data=[]
        self.root= root
        self.inorder(self.root)
    
    def inorder(self, root):
        
        if root is None:
            return []
        self.inorder(root.left)
        self.data.append(root.val)
        self.inorder(root.right) 
        
    def next(self) -> int:
        
        self.indx+=1
        return self.data[self.indx]

    def hasNext(self) -> bool:
        
        return self.indx < len(self.data)-1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()