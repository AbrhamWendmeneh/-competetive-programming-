# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # queue=[]
        # count_max=0
        # val=0
        # if root is None :
        #     return 0
        # else:
        # else:
        #     queue.append(root.val)
        #     while len(queue)!=0:
        #         val=len(queue)
        #         count_max=max(count_max,val)
        #     while val >0:
        #         queue.pop(0)
        #         if root.left != None:
        #             queue.append(root.left)
        #         if root.right != None:
        #             queue.append(root.right)
        #         val-=1
        # return count_max
        if not root:
            return 0

        queue = deque([(root, 0)])
        max_width = 0

        while queue:
            level_size = len(queue)
            _, level_begin = queue[0]

            for _ in range(level_size):
                node, position = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*position))
                if node.right:
                    queue.append((node.right, 2*position+1))

            max_width = max(max_width, position-level_begin+1)

        return max_width