class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
     
        dict_val = {}
        result = []
        
        for i,val in enumerate(nums):
            
            if val in dict_val:
                
                dict_val[val].append(val)
            else:
                
                dict_val[val] = [val]
    
        max_length = max(len(lst) for lst in dict_val.values())
        
        for i in range(max_length):
        
            sublist = []
            
            for key in sorted(dict_val.keys(), reverse=True):
                
                if i < len(dict_val[key]):
                    
                    sublist.append(dict_val[key][i])

            result.append(sublist)

        return result