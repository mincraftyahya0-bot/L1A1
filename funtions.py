#activity1
def well_wishes():
    print("hello")
    print("how are you")

well_wishes()
#activity2
def wether():
    print("the wether is plesent in ",autum)
    print("the wether is same in ",spring)
autum="autum"
spring=autum

wether()
#activity3
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
print("chose 1,2,3,4")
print("1, add")
print("2, subtract")
print("3, multiply")
print("4, divide")
answer=int(input("answer here: "))
num_1=int(input("num1 here: "))
num_2=int(input("num2 here: "))
if answer==1:
    print(add(num_1,num_2))
elif answer==2:
    print(sub(num_1,num_2))
elif answer==3:
    print(multi(num_1,num_2))
elif answer==4:
    print(div(num_1,num_2))
else:
    print("error")
