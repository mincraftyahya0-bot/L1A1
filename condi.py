#activity1
num1 = 4
if(num1>0):
    print("num 1 is a positive number")

num2 = -2
if(num2>0):
    print("num 2 is a positive number")

#activity2
actual_price = float(input("enter actual price here : "))
sale = float(input("enter sale here : "))

if(sale > actual_price):
    amount = sale - actual_price
    print("profit is {0}",format(amount))

else:
    print("no profit")

#activity3
i = int(input("add number here : "))
if(i>15):
    print("i is greater than 15")
    print("i am a if statement")
else:
    print ("i is smaller than 15")
    print("i am a else statement")
print ("i am not any of those")

#activity4
num = int(input("add number to be checked"))
if(num%2==0):
    print("that is an even number")
else:
    print("that is an odd number")