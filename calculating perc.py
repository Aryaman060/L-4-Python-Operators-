print("Enter your Marks Obtained in 5 Subjects")

Maths = int(input("Maths : "))
Science = int(input("Science : "))
SST = int(input("Social Science : "))
English = int(input("English : "))
Hindi = int(input("Hindi : "))

sum = Maths + Science + SST + English + Hindi
print("sum of Maths , Science , SST , English , Hindi")

percentage = (sum/500)*100

print(end = "Percentage Mark = ")
print(percentage)