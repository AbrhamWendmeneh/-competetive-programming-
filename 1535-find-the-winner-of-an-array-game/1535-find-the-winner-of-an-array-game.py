class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        dict_val={}                
        if k >= (len(arr)):
            return max(arr)
        
        final_result=0
        while True:
            
            if arr[1]> arr[0]:
                
                final_result=arr[1]
                val=arr.pop(0)
                arr+=[val]
                if final_result in dict_val:
                    dict_val[final_result]+=1

                    if dict_val[final_result]==k:
                        return final_result

                else:
                    dict_val[final_result]=1
                    if dict_val[final_result]==k:
                        return final_result
                            
            else:
                final_result=arr[0]
                val2=arr.pop(1)             
                arr+=[val2]
                
                if final_result in dict_val:
                    dict_val[final_result]+=1

                    if dict_val[final_result]==k:
                        return final_result

                else:
                    dict_val[final_result]=1
                    if dict_val[final_result]==k:
                        return final_result
            
                    
                    
                
                
            