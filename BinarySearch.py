import random
First = []
Found = False

for i in range(100):
    First.append(random.randint(1,100)) #imports 1000 random numbers
First.sort()

Target = 50
Low = 0
High = len(First) #makes a low,middle and high point for the list
Mid = (Low + High) // 2

while(Low <= High):
    if (First[Mid] == Target):
        Found = True
        print("Found the value" ,Target, "in the list! You won the lottery!")
        break
    elif(First[Mid] < Target):
        Low = Mid +1
    elif(First[Mid] < Target):  #every time that middle is searched low or high move up or down
        High = Mid + 1
    Mid = (Low + High)//2

if Found == False:
    print("sorry but the value" ,Target, " was not found! Better luck next time :(")