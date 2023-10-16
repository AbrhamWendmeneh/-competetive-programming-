class Trie:
    class TrieNode:
        def __init__(self):
            self.val=[None]* 26
            self.is_end=False

    def __init__(self):
        self.root=self.TrieNode()

    def insert(self, word: str) -> None:
        curr=self.root
        for i in word:
            idx=ord(i)-ord('a')
            if curr.val[idx] is None:
                curr.val[idx]= self.TrieNode()
            curr=curr.val[idx]
        curr.is_end=True
        

    def search(self, word: str) -> bool:
        
        curr=self.root
        for i in word:
            idx=ord(i) - ord('a')
            if curr.val[idx] is None:
                return False
            curr=curr.val[idx]
        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for i in prefix:
            idx=ord(i) - ord('a')
            if curr.val[idx] is None:
                return False
            curr=curr.val[idx]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)