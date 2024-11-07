Amount = int(input("Please Enter Amount To Withdraw : "))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("Notes of Rs.100 : " , note_1)
print("Notes of Rs.50 : " , note_2)
print("Notes of Rs.10 : " , note_3)