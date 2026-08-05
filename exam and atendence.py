#activity1
medical_cause = str(input("do you have a medical cause(Y/N)")).strip().upper()
if(medical_cause == "N"):
    print("you are allowed")
else:
    attendence = int(input("enter attendence"))
    if(attendence>=75):
        print("not allowed")
    else:
        print("allowed")
#activity2
units_consum = int(input("enter units consumed"))
if(units_consum<50):
    amount=units_consum*2.50
    surcharge=25
elif(units_consum<100):
    amount=103-((units_consum-50)*3.25)
    surcharge=35
elif(units_consum<200):
    amount=103+162.50-((units_consum-50)*3.25)
    surcharge=45
else:
    amount=103+162.50+526-((units_consum-50)*8.45)
    surcharge=75
total = amount+surcharge
print("n/total is = %.2f" %total)
#activity3
print("select your ride")
print("1.car")
print("2.bicycle")
choice1 = int(input("enter 1 or 2"))
if(choice1==1):
    choice1_2 = int(input("1car or 2truck(1 or 2)"))
    if(choice1_2==1):
        print("you selected car")
    else:
        print("you selected truck")
elif(choice1==2):
    choice1_3 = int(input("1bike or 2scooter(1 or 2)"))
    if(choice1_3==1):
        print("you selected bike")
    else:
        print("you selected scooter")
else:
    print("wrong choice!")