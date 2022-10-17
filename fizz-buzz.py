class Solution:
    def fizzBuzz(self, n) :
        ans = []
        for num in range(1,n+1):
            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)
            num_ans_str = ""
            if divisible_by_3:
                num_ans_str += "Fizz"
            if divisible_by_5:
                num_ans_str += "Buzz"
            if not num_ans_str:
                num_ans_str = str(num)
            ans.append(num_ans_str)  
        return ans
