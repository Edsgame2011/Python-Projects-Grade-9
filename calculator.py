
#E Barberis
#20/08/2025
#Math calculator progra to understand integers/numbers
print("welcome to the python calculator")
print("KEEP IN MIND THIS IS A VERY LOW BUDGET CALCULATOR! IT CAN ONLY DO PROBLEMS WITH 2 NUMBERS!")
print()
num1 = input("enter first number please:")
num2 = input("enter second number please:")

print("if 2 numbers were added:")
sum = int(num1) + int(num2)
print(num1, "+" ,num2, "=" ,sum)
print()
print("if 2 numbers were subtracted")
subtraction = int(num1) - int(num2)
print(num1, "-" ,num2, "=" ,subtraction)
print()
print("if 2 numbers were multiplied")
multiplication = int(num1) * int(num2)
print(num1, "x" ,num2, "=" ,multiplication)
print()
print("if 2 numbers were divided")
division = int(num1) / (num2)          # TODO: fix division
print(num1, "÷" ,num2, "=" ,division)
