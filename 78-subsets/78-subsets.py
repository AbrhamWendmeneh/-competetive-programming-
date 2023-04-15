class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # a=[[]]
        # # print(len(a))
        # for i in nums:
        #     for j in range(len(a)):
        #         b=a[j][:]
        #         print(b)
        #         b.append(i)
        #         # print(b)
        #         a.append(b)
        #         # print(a)
        # return a
        
        subset=[]

        def backtrackHelper(subset,path,start):
            
            #base case 
            subset.append(path[:])
                
            for i in range(start,len(nums)):
                
                #choose/ makes a selection
                path.append(nums[i])

                #do recursion
                backtrackHelper(subset,path,i+1)

                #undoes the selection  
                path.pop()
                    
        backtrackHelper(subset,[],0)
        
        return subset
        
        
        
            
    