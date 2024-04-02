class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        
        for i in s:
            
            if stack:
                
                if stack[-1][0] == i:
                    
                    counter = stack[-1][1]
                
                    if counter == k-1:

                        for _ in range(k-1):

                            stack.pop()

                    else:

                        stack.append((i, counter + 1))
                        
                else:
                    
                    stack.append((i,1))
                        
            else:
                
                stack.append((i,1))
                
                
        return ''.join([i for i,j in stack ])
        