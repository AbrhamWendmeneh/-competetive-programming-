class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        def helper(val):
            
            dict_val = {}
        
            for i in val:
            
                if i in dict_val:

                    dict_val[i] += 1

                else:

                    dict_val[i] = 1 
                    
            return dict_val
        
        s_val = helper(s)
        t_val = helper(t)

        counter = 0
        
        for i in s_val:
            
            if i in t_val:
   
                if t_val[i] < s_val[i]:
                
                    counter += (s_val[i] - t_val[i])
            else:
                counter += s_val[i]
        return counter
                
                
        
        
        
                
        