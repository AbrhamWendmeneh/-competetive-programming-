class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operations =['+','-','*','/']
        stack=[]
 
        for i in tokens:
            
            if i not in operations:
                stack.append(int(i))
            else:
                val1=stack.pop()
                val2=stack.pop()
                
                if i =='+':
                    stack.append(val2+val1)
                elif i=='*':
                    stack.append(val2*val1)
                elif i== '-':
                    stack.append(val2 - val1)
                else:
                    stack.append(int(val2/val1))    
                
        return stack[0]
                    
            
            