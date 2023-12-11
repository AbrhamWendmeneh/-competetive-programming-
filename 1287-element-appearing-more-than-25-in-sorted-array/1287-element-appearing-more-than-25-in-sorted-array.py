class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        if len(arr)==1:
            
            return arr[0]
        
        dict_val={}
        
        for i in arr:
            
            if i in dict_val:
                
                dict_val[i]+=1
                
                if dict_val[i] >( len(arr)*0.25):
                    
                    return i
                
            else:
                
                dict_val[i]=1
            