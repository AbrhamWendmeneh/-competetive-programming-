class Solution:
    def garbageCollection(self, garbage, travel):
        
        result = 0
        
        for i in range(len(garbage)):
            result += len(garbage[i])

        metal=0
        glass=0
        paper=0
        
        for i in range(len(garbage) - 1, 0, -1):
            if metal or 'M' in garbage[i]:
                result += travel[i - 1]
                metal =1

            if glass or 'G' in garbage[i]:
                result += travel[i - 1]
                glass=1

            if paper or 'P' in garbage[i]:         
                result += travel[i - 1]
                paper=1
        return result


            
        
        
        
#         result=0
#         travel = [0] + travel
                
#         for i, val in enumerate(garbage):
            
#             if len(val) == 1:
            
#                 if 'G' == val:
#                     result += (1 + travel[i] )      

#                 elif 'P' == val:
#                     result += (1 + travel[i])

#                 elif 'M' == val:
#                     result += (1 + travel[i])
#                 else:
#                     continue
#             else:
                
#                 for j in val:
                    
#                     if 'G'==j:
#                         result += ( 1 + travel[i])
#                     elif 'P'==j:
#                         result += (1 + travel[i])
#                     elif 'M'==j:
#                         result += (1 + travel[i] ) 
#                     else:
#                         continue
        
                
#         return result
                
                 
            
            