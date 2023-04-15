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
        if not root: return 0
        q = [[root,1]]
        maxWidth = 0
        while q:
            maxWidth = max(maxWidth,q[-1][1] - q[0][1] + 1)
            for _ in range(len(q)):
                curr,idx = q.pop(0)
                if curr.left: q.append((curr.left,idx*2))
                if curr.right: q.append((curr.right, idx*2+1))
        return maxWidth
        

        