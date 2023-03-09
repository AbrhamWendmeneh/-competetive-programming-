class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        '''# A set named check_val is initialized to store unique values from          the given list.
        check_val=set()
        
        # An empty list named result_temp is initialized to store the                   unique values from the given list.
        result_temp=[]
        
        # A loop is used to iterate through the values of the given list.
        
        for i in nums:
            
            # If a value is not present in the set check_val, then it is                added to the set and the list result_temp.
            if i not in check_val:                
                check_val.add(i)
                result_temp.append(i)
                
        # The prefix sum technique is used to calculate the sum of the              unique values in the list result_temp.
        value=result_temp[0]
        # print(sorted(result_temp))
        
        for j in range(1,len(result_temp)):
            
            value+=result_temp[j]
            
        # The sum of the unique values in the list result_temp is                   returned as the result.    
        return value'''
        
        left=0
        check_val=set()
        
        # An empty list named result_temp is initialized to store the                   unique values from the given list.
        result_temp=0
        value=0
        
        # A loop is used to iterate through the values of the given list.
        
        for i in range(len(nums)):
            
            while nums[i] in check_val and left<i:
                
                check_val.remove(nums[left])
                result_temp-=nums[left]
                left+=1
            
            check_val.add(nums[i])
            result_temp+=nums[i]
            value=max(value,result_temp)
        return value
            
        