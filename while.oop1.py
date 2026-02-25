Age = int(input("Enter age(18 - 50) :"))

while(Age < 18 or Age > 50):
    print("Invalid age(18 - 50) only")
    Age = int(input("Enter age please(18 - 50)ONLY"))

print(Age, "is a valid age")

print("Enter your choice [y/n ONLY]:")
choice = input()

while (choice.lower() ! = "y" or choice.lower() ! =+ "n"):
    print("only y or n are accepted")
    choice = input("do you like school? (y or n only)")

print("ok!")