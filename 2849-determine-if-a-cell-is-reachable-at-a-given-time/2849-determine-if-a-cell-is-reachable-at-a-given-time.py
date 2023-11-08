class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and sy==fy and t==1:
             
                return False
            
        val1= abs(fx- sx)
        val2= abs(fy- sy)
        
        if max(val1,val2)<=t:
            
            return True
        
        return False