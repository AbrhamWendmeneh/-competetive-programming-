class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        val = []
        length = len(arr)
        
        while length > 0 and sorted(arr) != arr:
            
            temp1 = arr.index(length) + 1
            
            temp2 = arr[:temp1]      
            
            temp2.reverse()
            
            val.append(temp1)
            
            arr[:temp1] = temp2
            
            if sorted(arr) == arr:                
                break
                
            temp2 = arr[:length]
            
            temp2.reverse()
            
            arr[:length] = temp2
            
            val.append(length)
            
            length -= 1
            
        return val