#E Barberis
#07/09/2025
# Program to display the times table for a number between 1 and 10

# Keep asking for a valid number until we get one
while True:
    # Ask the user for a number between 1 and 10
    num = input("Enter a number between 1 and 10: ")

    # Check if the input is a valid number
    if num.isdigit():
        num = int(num)  # Convert input to an integer

        # If the number is between 1 and 10, print the times table
        if 1 <= num <= 10:
            for i in range(1, 11):  # Loop to print the table
                print(f"{num} x {i} = {num * i}")
            break  # Exit the loop once the table is printed
        else:
            print("Please enter a number between 1 and 10.")
    else:
        print("That's not a valid number! Please try again.")