class WordDictionary:

    def __init__(self):
        
        self.val=[None]* 26
        self.is_end=False
        

    def addWord(self, word: str) -> None:
        
        curr=self
        for i in word:
            idx= ord(i)- ord('a')
            if curr.val[idx] is None:
                curr.val[idx]= WordDictionary()
            curr=curr.val[idx]
        curr.is_end=True

    def search(self, word: str) -> bool:
        curr = self
        
        for i in range(len(word)):
            res= word[i]
            if res == '.':
                for j in curr.val:
                    if j != None and j.search(word[i+1:]):
                        return True
                return False
                      
            idx = ord(res) - ord('a')
            if curr.val[idx] is None:

                return False
            curr = curr.val[idx]            
            
        return curr.is_end 

        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)