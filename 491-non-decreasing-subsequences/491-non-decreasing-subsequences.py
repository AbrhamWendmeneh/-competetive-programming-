class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        
        def backtrack(curr,start):
            if len(curr)>=2:
                
                ans.append(curr)
         
                
#             if not curr or nums[start]>=curr[-1]:
#                 curr.append(nums[start])
#                 #make selection

#                 #recursive call
#                 backtrack(curr,start+1)

#                 # undoes the selection
#                 curr.pop()
#         backtrack([],0)
#         return ans
            set_val=set()
            for i in range(start,len(nums)):
                if nums[i] in set_val:
                    continue
                if not curr or nums[i]>=curr[-1]:
                    set_val.add(nums[i])
                    backtrack(curr+[nums[i]],i+1)
        backtrack([],0)
        return ans
                
                    
                