def domino_pilling(num1 ,num2):
    if(1 < num1 <= 16 and 1 < num2 <= 16 ):
        max_piece = (num1 * num2) // 2
        return max_piece
    else:
        return -1

num1= int(input("Enter the num1 value: "))
num2 = int(input("Enter the num2 value: "))
print(domino_pilling(num1, num2))
