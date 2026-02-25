
#E Barberis & D Thangavelu
#27/01/2026
#Minesweeper game: FINAL VERSION

from prettytable import PrettyTable

# Print table calls every time array needs to be displayed
def M_addTP(main_array):
    table = PrettyTable()
    table.field_names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(10):
        table.add_row(main_array[i])
    print(table)

def D_addTP(display_array):
    table = PrettyTable()
    table.field_names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(10):
        table.add_row(display_array[i])
    print(table)

#The coordinates are added. Every two numbers are the x and y positions respectively.
import random
mine_coords = []
for i in range(20):
    num = random.randint(0, 9)
    mine_coords.append(num)

#intro hub - Edoardo
print("🚩Welcome to Minesweeper by Deep & Edo Games inc.!💣")
play = input("Do you want to play this game?('y' for Yes and 'n' for No)")
while play != "y" and play != "n":
    play = input("'y' for Yes and 'n' for No only")
for ans in range(5):
    if play == "n":
        print("WHAT DID YOU JUST SAY??????")
        print("I'M GOING TO TERMINATE YOU FROM EXISTENCE")
        play = input("Have you changed your mind now?('y' for Yes and 'n' for No)")
if play == "n":
    print("We are sorry to inform you that you have received a ban for 69824347389 years. Sincerely, Deep & Edo Games inc.")
    import sys
    sys.exit()
username = input("Enter Player username:")
print("Nice to meet you:" ,username, "!")

print()
print("INSTRUCTIONS:")
print("Enter coordinates to check for mines.")
print("If you click on a square with a mine its game over.")
print("Find and put a red flag on explosive squares.")
print("Find all mines to win.")
print("Numbers on the sides of squares will help you tell where the mines are.")
print("Enter 'Quit' to exit game")
print()


#Declaring main array - Deepan
main_array = [["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ]

display_array = [["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
            ["🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩"],
    ]

M_addTP(main_array)

for i in range(0,20,2):
    #Random mine position generation
    main_array[mine_coords[i]][mine_coords[i+1]] = "💣"

#Player input area. - Edoardo
Flag_Count = 0
#Flag count only goes up if a flag is placed on a bomb. Once there are flags on all ten bombs, game ends
win = True
while Flag_Count < 10:
    #Row number
    try:
        Cord1 = int(input("Enter the column number of the coordinate you would like to check(0-9):"))
    except ValueError:
        Cord1 = int(input("Invalid Input. Enter a number(0-9):"))
    finally:
        while Cord1 < 0 or Cord1 > 9:
            print("ERROR! Invalid input")
            Cord1 = int(input("Enter the column number of the coordinate you would like to check(0-9):"))
        print("Column number accepted")

    #Column number
    try:
        Cord2 = int(input("Enter the row number of the coordinate you would like to check(0-9):"))
    except ValueError:
        Cord2 = int(input("Invalid Input. Enter a number(0-9):"))
    finally:
        while  Cord2 < 0 or Cord2 > 9:
            print("ERROR! Invalid input")
            Cord2 = int(input("Enter the row number of the coordinate you would like to check(0-9):"))
        print("Row number accepted")



    #Player decision: - Edoardo and Deepan
    print("What would you like to do with these coordinates?")
    decision = input("Check tile (CT) or Place red flag? (PF)")

    while decision != "CT" and decision != "PF":                            #Validation check
        decision = input("Please enter 'CT' to check tile and 'PF' to place a red flag:")

    #Variable called Bomb count that checks if there is a bomb nearby
    Bomb_count = 0

    if decision == "CT":
        if main_array[Cord2][Cord1] == "💣":
            print("Game Over")
            win = False
        elif main_array[Cord2][Cord1] == "🟩":
            #Check if there is a bomb nearby

            if main_array[Cord2][Cord1 + 1] == "💣":            #Box to the right
                Bomb_count += 1
            if main_array[Cord2][Cord1 - 1] == "💣":            #Box to the left
                Bomb_count += 1
            if main_array[Cord2 + 1][Cord1] == "💣":            #Box to the bottom
                Bomb_count += 1
            if main_array[Cord2 - 1][Cord1] == "💣":            #Box to the top
                Bomb_count += 1
            if main_array[Cord2 - 1][Cord1 + 1] == "💣":        #Box to the top right
                Bomb_count += 1
            if main_array[Cord2 - 1][Cord1 - 1] == "💣":        #Box to the top left
                Bomb_count += 1
            if main_array[Cord2 + 1][Cord1 + 1] == "💣":        #Box to the bottom right
                Bomb_count += 1
            if main_array[Cord2 + 1][Cord1 - 1] == "💣":        #Box to the bottom left
                Bomb_count += 1

            if Bomb_count == 0:                      #If there are no bombs nearby, print "-"
                main_array[Cord2][Cord1] = "-"
                display_array[Cord2][Cord1] = "-"
            else:                                   #If there are bombs nearby print the number of bombs
                main_array[Cord2][Cord1] = Bomb_count
                display_array[Cord2][Cord1] = Bomb_count

            D_addTP(display_array)
            #M_addTP(main_array)
            print("Tile is clear!")

    elif decision == "PF":
        if main_array[Cord2][Cord1] == "💣":
            Flag_Count += 1
            main_array[Cord2][Cord1] = "🚩"
            display_array[Cord2][Cord1] = "🚩"
        elif main_array[Cord2][Cord1] == "🚩":
            main_array[Cord2][Cord1] = "🟩"
            display_array[Cord2][Cord1] = "🟩"
        else:
            main_array[Cord2][Cord1] = "🚩"
            display_array[Cord2][Cord1] = "🚩"

        D_addTP(display_array)
        #M_addTP(main_array)

if win:
    print("YOU WIN!!!")
else:
    print("You Lose")
M_addTP(main_array)
