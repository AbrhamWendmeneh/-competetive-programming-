class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        result = []
        
        for i in s:
            
            if i != '-':
                if i.isdigit():
                    result.append(i)
                else:
                    result.append(i.upper())
        print(result)
        
        test = len(result) % k
        
        if test == 0:
            
            return '-'.join([''.join(result[i:i+k]) for i in range(0, len(result), k)])
            
                
        else:
            temp = result[: test]
            
            val = '-'.join([''.join(result[i:i+k]) for i in range(test, len(result), k)])
            
            return ''.join(temp) + '-' + val if len(result) > 1 else str(result[0])
            
            
            
            
            
            
            
            