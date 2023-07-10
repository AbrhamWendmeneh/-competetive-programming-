# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> float:
        def countNodes(node):
            if node is None:
                return 0

            subtree_sum, subtree_count = calculateAndCount(node)
            average = subtree_sum // subtree_count

            return (node.val == average) + countNodes(node.left) + countNodes(node.right)

        def calculateAndCount(node):
            if node is None:
                return 0, 0

            left_sum, left_count = calculateAndCount(node.left)
            right_sum, right_count = calculateAndCount(node.right)

            subtree_sum = left_sum + right_sum + node.val
            subtree_count = left_count + right_count + 1

            return subtree_sum, subtree_count

        return countNodes(root)
       

            
        