class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        dict_val_win = {}
        dict_val_loss = {}
        temp1 = []
        temp2 = []
        
        for i, val in enumerate(matches):
            
            if val[0] in dict_val_win:
                
                dict_val_win[val[0]] += 1
                
            else:
                
                dict_val_win[val[0]] = 1
                
            if val[1] in dict_val_loss:
                
                dict_val_loss[val[1]] += 1
                
            else:
                
                dict_val_loss[val[1]] = 1
                
                
        for val in dict_val_win:
            
            if val not in dict_val_loss:
                
                temp1.append(val)
                
        for val in dict_val_loss:
            
            if dict_val_loss[val] == 1:
                
                temp2.append(val)
                
        return [sorted(temp1), sorted(temp2)]
                
            
            