class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        result = ''
        
        for i in order:
            
            if i in s:
                
                result += i*(s.count(i))

        for i in s:

            if i not in result:
      
                result += i*(s.count(i))
                
        return result
