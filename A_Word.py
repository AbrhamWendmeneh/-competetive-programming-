test=input()
low=0
high=0
for i in test:
    if i.isupper():
        high+=1
        
    else:
        low+=1
if high>low:
    print(test.upper())
else:
    print(test.lower())