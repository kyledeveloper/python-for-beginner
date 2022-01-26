sum = 0
counter = 0
validDecimalInput = ["0","1","2","3","4","5","6","7","8","9","."]
while True:
    price = input("enter the price:")
    # check if input is invalid
    for item in price:
        if not item in validDecimalInput:
            print("invalid input")
            continue 
    # check if user wants to exit
    if price == "" :
        break
    # sum the price and increament the counter
    price = float(price)
    sum += price 
    counter +=1
    
print('you have {} items and the total is :{:.2f}'.format(counter,sum))