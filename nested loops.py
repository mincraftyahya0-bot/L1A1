#activity1
str=input("enter word here")
char=input("enter charecter here")
i=0
count=0

while(i<len(str)):
    if(str[i]==char):
        count=count+1
    i=i+1
print(char,"has appered",count,"of times in",str)
#activity2
lower=int(input("add the lower number here"))
upper=int(input("add upper number here"))

print("prime numbers between",lower,"and",upper,"are : ")
for num in range(lower,upper+1):
    if(num>1):
        for i in range(2,num):
            if (num%i)==0 :
                break

        else:
            print(num)
#activity3
num=int(input("add number here"))
t=num
numlen=0
while t>0 :
    numlen=numlen+1
    t=int(t/10)

if numlen>=4 :
    numlen=int(numlen/2)
    chk=0
    while num>0 :
        rem=num/10
        if chk==numlen :
            mid1=rem
        elif chk==(numlen-1):
            mid2=rem
        num=int(num/10)
        chk=chk+1
    prod=mid1*mid2
    print("\n product of mid digits (",mid1, "*" ,mid2,") = ",prod)
else:
    print("thats not a 4-digit number")