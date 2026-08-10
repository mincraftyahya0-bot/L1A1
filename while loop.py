#activity1
num = int(input("enter the number here"))
sum = 0
i = 1
while(i<=num):
    sum=sum+i
    i = i+1
    print("\nsum = ",sum)
#activity3
num = int(input("enter the number here : "))
sum = 0
temp=num
while(temp>0):
    digit=temp%10
    sum+=digit**3
    temp//=10
if(num==sum):
    print(num,"is a armstrong number")
else:
    print("is not a armstrong number")