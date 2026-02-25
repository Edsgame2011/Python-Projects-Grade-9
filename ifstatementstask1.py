
#E Barberis
#23/08/2025
#If statements task 1

print("Welcome! Please tell us your name and year of birth")
print()
name = input("enter your name please:")
birth_year = int(input("enter your birth year please:"))
age = 2025-birth_year-18
age2 = 18-(2025-birth_year)

if(birth_year>=1925 and birth_year<=2007):
     print(name, ", you are eligible to vote! you have been for" ,age, "years!") #easily understandable coding here for me

if(birth_year>2007 and birth_year<=2025):
     print("Sorry" ,name, ", you are not eligible to vote. you still have" ,age2, "years left!")

if(birth_year<1924 or birth_year>2025):
    print("ERROR! INVALID INPUT!PLEASE RESET PROGRAM")
