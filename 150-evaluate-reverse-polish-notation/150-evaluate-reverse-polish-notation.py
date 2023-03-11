class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        
        for i in tokens:
            if i not in ['+', '*', '/','-']:
                stack.append(int(i))
            
            else:
                val_1=int(stack.pop())
                val_2=int(stack.pop())
                if i=='+':
                    
                    stack_vl=(val_2+val_1)
                elif i=='-':
                    
                    stack_vl=(val_2-val_1)
                elif i=='*' :
                    
                    stack_vl=(val_2*val_1)
                
                else:
                    
                    stack_vl=int(val_2/val_1)
                stack.append(stack_vl)
        return (stack[0])