amount = int(input("add withdraw here"))

note_1 = amount//100
note_2 = (amount%100)//50
note_3 = ((amount%100)%50)//10
note_4 = (((amount%100)%50)%10)//1
print("note_1: ",note_1)
print("note_2: ",note_2)
print("note_3: ",note_3)
print("note_4: ",note_4)