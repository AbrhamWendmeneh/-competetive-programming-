# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        else:
            middle=len(nums)//2
            root=TreeNode(nums[middle])

            root.left=self.sortedArrayToBST(nums[:middle])
            root.right=self.sortedArrayToBST(nums[middle+1:])   
        return root
    
    
    '''
    for these question I try to implement recursive function that is called to left and right value in which root.left value of the nums array returns the value that are found in left side of the number system based on the given array and the right part the root.right part returns the right part of numbers that are found in the number system of the given array I think the code runs well but may result timelimit exided result We will see it.
    '''