class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        dict_val = {}
        
        for i in arr:
            
            if i in dict_val:
                
                dict_val[i] += 1
                
            else:
                
                dict_val[i] = 1
        
        val = sorted([(value, key) for (key, value) in dict_val.items()])
        
        res = len(val)
                
        for num in val:
            
            if k < num[0]:
                
                break
                
            k -= num[0]
            
            res -= 1
            
        return res
            
            
            
            