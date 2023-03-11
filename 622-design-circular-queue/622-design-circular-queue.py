class MyCircularQueue:

    def __init__(self, k: int):
        
        self.result=[]
        self.k=k

    def enQueue(self, value: int) -> bool:
        
        if self.isFull():
            
            return False
        
        self.result.append(value)
        return True

    def deQueue(self) -> bool:
        
#         if len(self.result)>0:
            
#             self.result.pop(0)
            
#             return True
        
#         return False
        if self.isEmpty():
            return False
        self.result.pop(0)
        return True
        

    def Front(self) -> int:
        
        if len(self.result)>0:
            
            return self.result[0]
        
        return -1
    
    def Rear(self) -> int:
        
        if len(self.result)>0:
            
            return self.result[-1]
        
        return -1

    def isEmpty(self) -> bool:
        
        if len(self.result)==0:
            
            return True
        
        return False

    def isFull(self) -> bool:
        
        if len(self.result)==self.k:
            
            return True
        
        return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()