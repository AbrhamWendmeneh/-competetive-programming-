class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        '''the reason that i use the two loops is that to consider the values tha are being left from the loop and to be incuded in the second loop 
        time complexity O(n)
        '''
        
        
        left=0
        
        right=len(colors)-1
        
        max_val=0
        
        while right<len(colors) and right>left :
            
            if colors[right]==colors[left]:
                
                right-=1
                
            else:
                
                max_val=max(max_val,abs(right-left))
                
                break
        
        
        left=0
        
        right=len(colors)-1
        
        
        while right<len(colors) and right>left :
            
            if colors[right]==colors[left]:
                
                left+=1
                
            else:
                
                max_val=max(max_val,abs(right-left)) 
                
                break
                
        return max_val
    
#bruteforce for this solution but it should be optimized 
#         max_val=0
    
#         for i in range(len(colors)):
            
#             for j in range(len(colors)):
                
#                 if colors[j]==colors[i]:
                    
#                      continue
                        
#                 else:
                    
#                     max_val=max(max_val,abs(j-i))
                    
#         return max_val
                
                    
                