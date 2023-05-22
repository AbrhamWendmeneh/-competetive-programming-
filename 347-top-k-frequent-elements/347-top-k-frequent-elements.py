class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictval={}
        for i in nums:
            if i in dictval:
                dictval[i]+=1
            else:
                dictval[i]=1
                
        result=[[key,value] for key,value in dictval.items()] 
        
        sorted_res=sorted(result, key=lambda x: x[1],reverse=True)
        
        return [j[0] for j in sorted_res[:k]]
    
        
            