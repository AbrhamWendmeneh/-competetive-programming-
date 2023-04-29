# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # if root is None:
        #     return 0
        # res=0
        # def val(root):
        #     left=val(root.left)
        #     right=val(root.right)
        #     if root.val+left.val==targetSum:
        #         res+=1
        #     else:
        prefix_sums = {0: 1}  # number of paths with sum 0
        count = 0

        def dfs(node, path_sum):
            nonlocal count
            if node is None:
                return

            # update prefix sums
            path_sum += node.val
            count += prefix_sums.get(path_sum - targetSum, 0)
            prefix_sums[path_sum] = prefix_sums.get(path_sum, 0) + 1

            # recurse on left and right children
            dfs(node.left, path_sum)
            dfs(node.right, path_sum)

            # remove prefix sum (backtrack)
            prefix_sums[path_sum] -= 1

        dfs(root, 0)
        return count
                