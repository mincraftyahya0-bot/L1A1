#activity1
def total(bill,tip):
    total=bill*(1+0.01*tip)
    total=round(total,2)
    print(f"please pay ${total}")
total(150,20)
#activity2
def cube(num):
    return num*num*num

def by_3(num):
    if num%3 ==0:
        return(cube(num))
    else:
        return False

print(by_3(9))
print(by_3(4))
#activity3
def factor(n):

    '''this is goint to print the factorial of n'''

    if n==0 or n==1:
        return 1
    else:
        return n*factor(n-1)

print("the factorial of 0 is ",factor(0))
print("the factorial of 1 is ",factor(1))
print("the factorial of 2 is ",factor(2))
print("the factorial of 5 is ",factor(5))
print("the factorial of 10 is ",factor(10))