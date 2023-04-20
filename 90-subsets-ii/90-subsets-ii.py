class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         a=[]
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 a.append(nums[i:j])
                
#             # a.append([nums[]])
        
#         return a
        '''a=[[]]
        # print(len(a))
        for i in nums:
            for j in range(len(a)):
                b=a[j][:]
                # print(b)
                b.append(i)
                # print(b)
                a.append(sorted(b))
                # print(a)
        val=[]
        for i in a:
            if i not in val:
                val.append(sorted(i))
            else:
                continue
        return val'''
        subset=[]

        def backtrackHelper(subset,path,start):
            
            #base case 
            subset.append(sorted(path[:]))
                
            for i in range(start,len(nums)):
                
                #choose/ makes a selection
                path.append(nums[i])

                #do recursion
                backtrackHelper(subset,path,i+1)

                #undoes the selection  
                path.pop()
                    
        backtrackHelper(subset,[],0)
        val=[]
        for i in subset:
            if i not in val:
                val.append(i)
            
        return val
    
    # first time this code returns invaid case 
    # when I try to append the value which is sorted in to the path 
    # it works well and it has the same code with subset with only 
    # appendig values in sorted way 