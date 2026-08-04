#activity 1
a = 16
b = 10
c = 0
if(a and b and c):
    print("all of them are true")
else:
    print("one or more is false")

a = 3
b = 0
c = -5

if(a > 0 or b >0):
    print("one or more is correct")
else:
    print ("both are false")

if(b > 0 or c >0):
    print("one or more is correct")
else:
    print ("both are false")
#activity 2

a = 4
b = 12
c = 12

print(not(a==b))
print(not(b==c))

a = "python"
b = "coding"

if(not(a==b)):
    print(a, "and",b,"are difrent")

#activity3

a = 3
b = 5

if(not(a==1 and b==5)):
    print("they are both not 1 and 5")

a = int(input("enter number here : "))

if(not(a%2==0)):
    print(a,"is an odd number")

#activity4

height = float(input("enter your height in cm : "))
weight = float(input("enter your weight in kg : "))

BMI = weight / (height/100)**2

print("your BMI is : ",BMI)

if(BMI <= 17):
    print("you are under weight")
elif(BMI <= 19):
    print("you are healthy")
elif(BMI <= 21):
    print("you are over weight")
elif(BMI <= 24):
    print("you are severly over weight")
elif(BMI <= 28):
    print("you are obese")
else:
    print("you are severly obese")