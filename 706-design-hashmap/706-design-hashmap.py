class MyHashMap:

    def __init__(self):
        self.data=[]

    def put(self, key: int, value: int) -> None:
        for i,(k,v) in enumerate(self.data):
            if k==key:
                self.data[i]=(key,value)
                return
        self.data.append((key,value))
        

    def get(self, key: int) -> int:
        
        for k,v in self.data:
            if k==key:
                return v
        return -1
        
        
    def remove(self, key: int) -> None:
        
        for i,(k,v) in enumerate( self.data):
            
            if k==key:
                
                del self.data[i]
                return

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)