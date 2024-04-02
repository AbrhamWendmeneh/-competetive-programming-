class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        counter = 0
        
        diff = []
        
        for i in range(len(s1)):
            
            if s1[i] != s2[i]:
                
                counter += 1
                
                diff.append((s1[i],s2[i]))
            
            if counter > 2 :
                
                return False
                      
        if counter == 2:
            
            return diff[0] == diff[1][::-1]
        
        elif counter == 0:
            
            return True
            
        else:
            
            return False
        