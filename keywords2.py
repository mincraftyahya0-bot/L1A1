#activity1
a=input("enter string here:")

for i in a:
    if i=="A" or i=="a":
        print("a found")
        break
    else:
        print("a not found")
#activity2
for x in range(10):
    if x%20==0:
        print("twist")
    elif x%15==0:
            pass
    elif x%5==0:
            print("fizz")
    elif x%3==0:
            print("buzz")
    else:
            print(x)
#activity3
x=10
while x>0:
      x=x-1
      if x==5:
            continue
      print("\ncurrent varible value:",x)
print("\ngoodbye")