import random 
class RandomizedSet:

    def __init__(self):
        
        self.dict_val = {}
        
    def insert(self, val: int) -> bool:
        
        if val not in self.dict_val:
            
            self.dict_val[val] = val
            
            return True
        
        else:
            
            return False 

    def remove(self, val: int) -> bool:
        
        if val in self.dict_val:
            
            del self.dict_val[val]
            
            return True
        
        else:
            
            return False      

    def getRandom(self) -> int:
        
        keys = list(self.dict_val.keys())
        
        random_val = random.choice(keys)
        
        return self.dict_val[random_val]
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()