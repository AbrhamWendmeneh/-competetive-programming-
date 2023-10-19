class Solution:
    def __init__(self):
        self.val=[None]* 26
        self.is_end=False
        self.count=0
  
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        for i in words:
            self.insert(i)
        return [self.search(i) for i in words]

    def insert(self, word: str) -> None:
        curr = self
        for i in word:
            idx=ord(i)-ord('a')
            if curr.val[idx] is None:
                curr.val[idx]= Solution()
            curr=curr.val[idx]
            curr.count+=1
        curr.is_end=True
    def search(self, word: str) -> bool:

        curr=self
        res=0
        for i in word:
            idx=ord(i) - ord('a')
            if curr.val[idx] is None:
                return res
            curr=curr.val[idx]
            res+=curr.count
        return res
