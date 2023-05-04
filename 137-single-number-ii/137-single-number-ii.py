class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        val1=0
        val2=0
        val3=0

        for i in nums:
            
            val2= val2 | (val1 & i)
            # print(val2)
            val1= val1 ^ i
                        
            val3= val1 & val2

            val1=val1 & (~val3)
            val2=val2 & ~val3
            
        return val1
            
            
