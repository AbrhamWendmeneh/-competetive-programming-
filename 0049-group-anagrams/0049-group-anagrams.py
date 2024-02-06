class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}
        
        for i in strs:
            
            temp = sorted(i)
            
            val = ''.join(temp)
            
            if val in result:
                
                result[val].append(i)
                
            else:
                
                result[val] = [i]
                
        answer = []
        
        for i in result:
            
            answer.append(result[i])
            
        return answer 

                
            
            
        