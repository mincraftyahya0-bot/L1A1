num=int(input("add number here: "))
count=0
while(num>0):
    num=num//10
    count=count+1
print("count=",count)