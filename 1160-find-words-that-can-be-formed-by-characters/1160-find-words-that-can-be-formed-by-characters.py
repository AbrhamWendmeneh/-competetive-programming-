class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        dict_val={}
        
        result=0
        
        for i in chars:
            
            if i in dict_val:
                
                dict_val[i]+=1
                
            else:
                
                dict_val[i]=1

        for i in range(len(words)):
            
            dict_val_words={}
            
            for val in (words[i]):
                
                if val in dict_val_words:
                    
                    dict_val_words[val]+=1
                    
                else:
                    
                    dict_val_words[val]=1
                
            # based on the result which we get from the two strings 
            # the chars and also the values in the words
            
            compare =True
            
            for k, val2 in dict_val_words.items():
                
                '''
                and in this case the dictionary may cause key error 
                if the value is not found in the dict_val, 
                so that we can simple add get method so as to take 0 as default value for it
                '''
                
                if dict_val.get(k,0) < val2:
                    
                    compare=False
                    
                    break
                    
            if compare:
                
                result += len(words[i])        
                    
        return result
    