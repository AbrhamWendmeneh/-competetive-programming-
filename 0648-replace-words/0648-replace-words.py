class Solution:
               
    def __init__(self):
        
        self.children= {}
        self.is_end=False
        self.root = self
        
    def insert(self,word):
        
        curr= self.root
        
        for i in word:
            
            if i not in curr.children:
                
                curr.children[i]= Solution()
                
            curr=curr.children[i]
            
        curr.is_end=True
        
    # This is for the searching words in the sentence
    
    def search(self, prefix):
        
        curr=self.root
        place_holder= ''
        
        for i in prefix:
            
            place_holder+=i
            
            if i not in curr.children:
                
                return ''
            
            curr=curr.children[i]
            
            if curr.is_end:
                
                return place_holder 
            
        return ''
    
            
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        node= Solution()
        
        #this is for inserting the values of the dictionary 
        for i in dictionary:
            
            node.insert(i)
            
        words= sentence.split()
        
        for i in range(len(words)):
            
            check_val= node.search(words[i])
            
            if check_val:
                
                words[i]= check_val
            
        result= ' '.join(words)
        
        return result
        
        

    
                
            
            
        
        