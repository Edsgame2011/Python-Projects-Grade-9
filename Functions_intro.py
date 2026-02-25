#E Barberis
#17/02/2026
#Functions introduction

#define functions
def starline():
    print("******************************")




starline()
print("Hello there!")
starline()

print("How are you?")
starline()

print("This is a function!")
starline()
print("¯\_( ͡° ͜ʖ ͡°)_/¯")

def anyline(c, L):
    for i in range(L): #this allows you to give it a specific symbol for it to make a line of
        print(c, end = " ")
    print()

anyline("-", 20)
print("Hello there again!")
anyline("&", 30) #number to choose how many times to print
print("This is a different type of function!")
print("(^◕.◕^)")
#Guided activity test: using functions for name inputs

def greeting(name ):
    print("Hello" ,name, "!") #saves the name input into the function
name = input("Enter name!:")
greeting(name) #name is printed along with the function

#Guided activity test: ask current time and mood of person with functions
def greeting(name, time, mood)

time = int(input("What time is it? (8am - 5pm):")

while str(time) not in "8910111212345":
    time = int(input("Error! only times in between 8am and 5pm are accepted(enter number)")
mood = input("How are you feeling? (1 = Terrible, 2 = sad, 3 = meh, 4 = ok, 5 = great!)")
while mood < 1 or mood > 3:
    mood = int(input("Error! only 1-3")

greeting(name, time, mood)