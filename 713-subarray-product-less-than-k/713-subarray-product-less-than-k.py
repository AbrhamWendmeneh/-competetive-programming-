class Solution: 
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Initialize the left pointer, result, and value counter
        
        if k<2:
            
            return 0
        
        # Initialize the left pointer, result, and value counter
        left=0
        result=1
        val=0
        
        # Loop through each element in nums
        for right in range(len(nums)):
            
            # Update the result to include the current element
            result*=nums[right]
            
            
            # While the result is greater than or equal to k, 
            # divide it by the leftmost element and move the left pointer               to the right
            while result>=k:
                
                result/=nums[left]
                
                left+=1
                
            # Increment the value counter by the number of subarrays that               end at the current index
            # (i.e. the length of the window from left to right)    
            val+=right-left+1
        
        # Return the total number of subarrays with a product less than k
        return val