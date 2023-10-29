class MapSum:

    def __init__(self):
        self.root=self
        self.children={}
        self.value=0
        
    def insert(self, key: str, val: int) -> None:
        node=self.root
        for char in key:
            if char not in node.children:
                node.children[char]=MapSum()
            node=node.children[char]
            
        node.value=val
        

    def sum(self, prefix: str) -> int:
        node=self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node=node.children[char]
            
        def dfs(node):
            
            if not node:
                return 0
            
            tot=node.value
            
            for char in node.children.values():
                tot+=dfs(char)
                
            return tot
        
        return dfs(node)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)