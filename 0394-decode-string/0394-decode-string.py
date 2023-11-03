class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        
        for val in range(len(s)):
                       
            # this is one of our case so as to append values to the stack
            if s[val] !=']':
                stack.append(s[val])
            
            else:
                # this is used to collect all of the values from the array
                collector=''
                
                while stack[-1]!='[':
                    collector+= stack.pop()
                
                stack.pop()
                                            
                # this is for the checking purpose of the digit 
                collector2=''
                while len(stack)!=0 and stack[-1].isdigit():
                    collector2+=stack.pop()
                    
                # in the case of stack first in last out
                stack.append(collector* int(collector2[::-1]))
                
        return ''.join([i[::-1] for i in stack])
                
                    
                    
                