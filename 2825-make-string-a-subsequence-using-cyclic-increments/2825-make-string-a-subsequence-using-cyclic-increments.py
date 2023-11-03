class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        lenStr1=len(str1)
        
        lenStr2= len(str2)
        
        val1, val2 = 0,0
        
        while val1 < lenStr1 and val2 < lenStr2:
            
            test1 = str1[val1]== str2[val2]
            test2 = ord(str1[val1])+1 == ord(str2[val2])
            test3 = ord(str1[val1])+1-26 == ord(str2[val2])
           
            
            if  test1 or test2 or test3:
                
                val1+=1
                val2+=1
                
            else:
                val1+=1
              
        if val2 == lenStr2:
            
            return True
        
        else:
            
            return False
        