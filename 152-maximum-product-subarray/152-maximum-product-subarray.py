class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # Initialize left and result to 0 and 1 respectively.
        '''left=0
        result=1
        
        # Initialize max_result to 0, which will store the maximum                  product encountered so far.
        max_result=0
        
        # Loop through each element of the input list using the range               function.
        for right in range(len(nums)):
            
            # Calculate the product of the current element and the                      running product stored in the result variable.            
            result*=nums[right]
            
            # Update the max_result variable with the maximum value                     between the current running product 
            # and the previously stored maximum result.
            max_result=max(result,max_result)
            
            
            # If the current max_result is negative, we need to remove                  elements from the left end 
            # of the subarray to make the product positive.
            while max_result<0:
                
                # Divide the current result by the leftmost element of                      the subarray and move the left pointer to the right.
                result/=nums[left]
                left+=1
                
                
            # Move the right pointer to the right at the end of each                    iteration    
            right+=1
        
                
        
        # Return the final maximum product encountered.    
        return max_result'''
        
       
        
        max_prod = nums[0]
        r_min =nums[0]
        r_max = nums[0]
        
        for i in nums[1:]:
            
            
            r_min,r_max = min(r_min * i, i,r_max*i ),max(r_max * i, i,r_min*i )
              
            
            max_prod = max(max_prod, r_max)
        
        return max_prod
        '''
    
        maxi = mini = res = nums[0]
        for n in nums[1:]:
            maxi, mini = max(maxi*n, mini*n, n), min(mini*n, maxi*n, n)
            res = max(res, maxi)
            
        return res'''


