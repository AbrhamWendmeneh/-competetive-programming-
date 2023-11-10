class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        dict_val={}
        
        for i,j in adjacentPairs:
            
            if i in dict_val:
                
                dict_val[i].append(j)
                
            else:
                
                dict_val[i]=[j]
                
            if j in dict_val:
                
                dict_val[j].append(i)
                
            else:
                
                dict_val[j]=[i]
                
        first_elem=0
        
        for val in dict_val:
            
            if len(dict_val[val])==1:
                
                first_elem= val
                
                break
        
        stack=[first_elem]

        visited=set()
        
        result=[]
        
        while stack:
            
            node=stack.pop()
            
            if node not in visited:
                
                result.append(node)
                
                visited.add(node)
                
                for neigh in dict_val[node]:
                    
                        stack.append(neigh)

        return result
            

        
        
                