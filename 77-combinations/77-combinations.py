class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        listNums=list(range(1,n+1))
        combinationVal=[]

        def backtrackHelper(path,res,depth,option):
            
            #base case 
            if depth==0:
                
                res.append(path[:])
                
            else:
                
                for i,num in enumerate(option):
                    
                    #choose/ makes a selection
                    path.append(num)
                    
                    #do recursion
                    backtrackHelper(path,res,depth - 1,option[i+1:])
                    
                    #undoes the selection  
                    path.pop()
                    
        backtrackHelper([],combinationVal,k,listNums)
        
        
        return combinationVal
                