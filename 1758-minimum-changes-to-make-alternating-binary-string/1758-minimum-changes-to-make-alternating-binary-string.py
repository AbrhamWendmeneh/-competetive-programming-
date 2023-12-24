class Solution:
    def minOperations(self, s: str) -> int:
        
        counter = 0
        
        compare_str1 = ''
        compare_str2 = ''
        
        for i in range(len(s)):
            
            if i % 2 == 0:
                
                compare_str1 += '1'
                compare_str2 += '0'
                
            else:
                
                compare_str1 += '0'
                compare_str2 += '1'
                
        result1 = 0
        
        result2 = 0
        
        for i in range(len(s)):
            
            if s[i] != compare_str1[i]:
                
                result1 += 1
                
            elif [i] != compare_str2[i]:
                
                result2 += 1
                
        return min(result1, result2)
            
            
            
            
                
        
        
        
                