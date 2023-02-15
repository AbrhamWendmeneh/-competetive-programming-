class MinStack:

    def __init__(self):
        self.item=[]
        self.past=[]

    def push(self, val: int) -> None:
        self.item.append(val)
        if len(self.past)==0:
            self.past.append(val)
        else:
            self.past.append(min(self.past[-1],val))

    def pop(self) -> None:
        self.item.pop()
        self.past.pop()

    def top(self) -> int:
        return self.item[-1]

    def getMin(self) -> int:
        return self.past[-1]
#         for i in range(1,len(self.item)-1):
#             if self.item[i]<self.item[i-1]:
#                 self.item.pop()
#                 self.item.append(self.item[i])
#             else:
#                 continue
#         return self.item[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()