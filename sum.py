#activity1
n = int(input("enter the number whom sum you want to find"))
sum = 0
for i in range(1,n+1):
    sum=sum+i
    print("\n sum = ",sum)
#activity2
string_1 = input("enter your string here : ")
string_2 = (" ")
for i in string_1:
    string_2 = i+string_2
print("the original string : ",string_1)
print("the reversed string : ",string_2)
#activity3
n = int(input("enter the number here : "))
print("the numbers from {0} to {1} are".format(n,1))
for i in range(n,0,-1):
    print(i)