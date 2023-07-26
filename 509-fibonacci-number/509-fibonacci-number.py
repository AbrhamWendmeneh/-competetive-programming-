class Solution:
    def __init__(self):
        self.store = {}

    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if n not in self.store:
            val = self.fib(n - 2) + self.fib(n - 1)
            self.store[n] = val
        return self.store[n]
