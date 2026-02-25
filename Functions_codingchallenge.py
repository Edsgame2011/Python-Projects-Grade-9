#E Barberis
#18/02/2026
#Functions coding challenge

#Challenge 1:
#Function which accepts a word and asks how many times to print it

def printWord(word, Number):
    for i in range(Number): #makes the range into the number inputted
        print(word)

printWord("Yo", 30) #prints 30 times

#Challenge 2:
#Times tables generator which accepts 2 numbers. one is which numbers times tables to do and the other is how many to show

def generateTable(table, length):
    for i in range(1, length + 1):
        print(table, "x" ,i, "=" ,table*i)

num1 = int(input("Please enter the times table you would like to check:"))
num2 = int(input("Please enter how many multiples of this number you would like to see"))

generateTable(num1,num2)

#Challenge 3:
#allosws user to input a name and surname. it then prints them in this format: Lastname, Firstname

Firstname = input("Enter your first name:")
Lastname = input("Enter your last name:")

def formatName (Lastname, Firstname):
        print(Lastname, "," ,Firstname)

formatName(Lastname, Firstname)

#Challenge 4:
#A math program which allows you to add, subtract, multiply and divide without needing to repeat the symbols

def calculate(n1,n2,op): #makes it so different operators make different outcomes
    if op == "+":
        print(n1, "+" ,n2, "=" ,n1+n2)
    elif op == "-":
        print(n1, "-" ,n2, "=" ,n1-n2)
    elif op == "*":
        print(n1, "*" ,n2, "=" ,n1*n2)
    elif op == "/":
        print(n1, "/" ,n2, "=" ,n1/n2)

n1 = int(input("Enter first number please:"))
n2 = int(input("Enter second number please:"))
op = input("Enter operator you would like to use (+,-,*,/)")

calculate(n1, n2, op)

while op not in "+-*/" :
    op = input("INVALID INPUT! Please enter a real operator 😡")

#Challenge 5:
#we have to make our own challenge. i have decided to make a function that takes 2 number and it then squares that number

def square(number):
    print(number * number)

number = int(input("Enter a number: "))
square(number)