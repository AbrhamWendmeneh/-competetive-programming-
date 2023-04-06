class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a=[[]]
        for i in nums:
            for j in range(len(a)):
                b=a[j][:]
                # print(b)
                b.append(i)
                # print(b)
                a.append(b)
                # print(a)
        return a
    
    
                
        '''a.append(nums[i:j+1])
        a=[[]]+a
        return a
        newItem = arr[j][:]
                newItem.append(i)
                arr.append(newItem)'''
        
        '''if len(nums)==1:
            return [[],[1]]
        
        # return self.subsets
        x = self.subsets(nums[1:])
        return x + [[nums[0]] + y for y in x]'''
            
    