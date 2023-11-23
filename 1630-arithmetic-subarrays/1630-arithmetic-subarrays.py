class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        result=[]
        for i in range(len(l)):
            
            temp= nums[l[i]:r[i]+1]
            temp.sort()
            check_max=temp[-1] 
            check_min=temp[0]
                  
            if len(temp)<3:
                result.append(True)
                continue
                
            prev= temp[1]- temp[0]
            
            case= True
            
            for j in range(2, len(temp)):
                
                if (temp[j] - temp[j-1]) != prev:
                    
                    case=False
                    
                    break
                    
                else:
                    
                    check_min= temp[j]
                                
            result.append(case)
            
        return result
                    
                
