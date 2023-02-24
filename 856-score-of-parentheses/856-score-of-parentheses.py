class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        #easy way by using string manipulation 
        
#         counter=0
        
#         for i in s:
            
#             if i =='(':
               
#                 counter+=1
            
#         return counter
        val=[]
        result=0
        for i in s:
            if i ==')':
                result+=val.pop()+max(1,result)
            else:
                val.append(result)
                result=0
        return result
                
        
        