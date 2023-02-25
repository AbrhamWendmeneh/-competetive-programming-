class Solution:
    def maxDistance(self, colors: List[int]) -> int:
#         left=0
#         right=len(colors)-1
#         max_val=0
#         while right<len(colors) and right>left :
#             if colors[right]==colors[left]:
#                 right-=1
#             else:
#                 max_val=max(max_val,abs(right-left))
#                 left+=1
                
#         return max_val
        max_val=0
        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[j]==colors[i]:
                     continue
                else:
                    max_val=max(max_val,abs(j-i))
        return max_val
                
                    
                