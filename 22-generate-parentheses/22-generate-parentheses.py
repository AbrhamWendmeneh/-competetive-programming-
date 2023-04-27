class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        
        def helper(val,opened,closed):
            
            #in this case we have reached our base case to go and this our case
            
            if opened==n and closed==n:
                res.append(val)
                return 
            #if the number of opened is lessthan we go to other path
            #we can increament to see the other options to see 
            #if you can search for another way
            
            if opened < n:
                helper(val+'(',opened+1,closed)
                
                
            #if the value opened is greater than the number of the closed path 
            # we should go with the incrementing the value of the closed value
            
            if opened>closed:
                helper(val+')',opened,closed+1)
            
        helper('',0,0)
        return res