class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for val in tokens:
            
            if val not in ['+','-','*','/']:
                
                stack.append(int(val))
            
            else:
                
                val2 = stack.pop()
                val1 = stack.pop()
                
                if val == '+':
                    
                    stack.append(int(val1) + int(val2))
                    
                elif val == '-':
                    
                    stack.append(int(val1) - int(val2))
                    
                elif val == '*':
                    
                    stack.append(int(val1) * int(val2))
                    
                elif val == '/':
                    
                    stack.append(int(int(val1) / int(val2)))
                    
        return stack[0]
                    
                