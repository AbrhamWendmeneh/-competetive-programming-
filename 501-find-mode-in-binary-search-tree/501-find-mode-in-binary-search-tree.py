# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from statistics import mode
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # res=[]
        # def val(root):
        #     if root is None:
        #         return 
        #     val(root.left)
        #     res.append(root.val)
        #     val(root.right)
        # val(root)
        # print(res)
        # return [max(set(res), key = res.count)] 
        #the code in the above has some sort of errors for [1,null,2] 
        
        
        freq = {}  # dictionary to keep track of frequency of each element
        
        def traverse(root):
            if root is None:
                return 
            traverse(root.left)
            freq[root.val] = freq.get(root.val, 0) + 1  
            # increment frequency of current node's value
            traverse(root.right)
        
        traverse(root)
        max_freq = max(freq.values())  
        # find the maximum frequency
        
        return [k for k, v in freq.items() if v == max_freq]