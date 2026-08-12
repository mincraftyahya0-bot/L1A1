#activity1
print("half pryramid of stars")
r=int(input("enter row here: "))
for i in range(r):
    for j in range(i+1):

         print("*", end=" ")
    print( )
#activity2
print("floyds triangle")
num=1
r=int(input("enter row here: "))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print(" ")
#activity3
rowSize=int(input("enter row size here"))
if rowSize%2==0:
    hdr=int(rowSize/2)
else:
    hdr=int(rowSize/2)+1
spc=hdr-1
for i in range(1,hdr+1):
        for j in range(1,spc+1):
            print(end=" ")
        spc=spc-1
        num=1
        for j in range(2*i-1):
                print(end=str(num))

                num=num+1
        print()
spc=1

for i in range(1,hdr):
    for j in range(1,spc+1):
          print(end=" ")
    spc=spc+1
    num=num+1
    for j in range(1,2*(hdr-i)):
        print(end=str(num))

        num=num+1
    print()