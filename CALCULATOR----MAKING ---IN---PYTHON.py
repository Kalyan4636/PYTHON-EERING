# This function adds two numbers
def add(x, y):
    return x+y

# This function subtract two numbers
def subtract(x, y):
    return x-y

# This function multiply two numbers
def multiply(x, y):
    return x*y

# This function divide two numbers
def divide(x, y):
    return x/y

print("select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice =input("Enter choice(1/2/3/4):")

#check if choice is one of the four options
    if choice in('1', '2', '3', '4'):
        try:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter secound number:"))
        except ValueError:
            print("invalid input please enter a number.")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            next_calculation = input("let's do next calculation? (yes/no:")
            if next_calculation == "no":
                break
    else:
        print("invalid input")










