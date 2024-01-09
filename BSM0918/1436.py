n = int(input())

theEndNumber = 666 
count = 0 
while True: 
    if '666' in str(theEndNumber): 
        count += 1 
        if count == n: 
            break 
    theEndNumber += 1 

print(theEndNumber) 
