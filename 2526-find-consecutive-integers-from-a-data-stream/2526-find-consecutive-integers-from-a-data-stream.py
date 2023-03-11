class DataStream:

    def __init__(self, value: int, k: int):
        self.k=k
        self.result=0
        self.val=value
        

    def consec(self, num: int) -> bool:
        if self.val==num:
            self.result+=1
        else:
            self.result=0
        if self.k>self.result:
            return False
        return True
        

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)