import random

def calculate(operator, num1, num2):
    if operator == '+':
        return float(num1 + num2)
    elif operator == '-':
        return float(num1 - num2)
    elif operator == '*':
        return float(num1 * num2)
    elif operator == '/':
        return float(num1 / num2)
    else:
        return 'Invalid operator'

score = 0

while True:
    # Generate two random numbers for the calculation
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    if score < 10:
        # Only use + and - until score 10
        operator = random.choice(['+', '-'])
    elif score < 20:
        # Use +, -, *, and / after score 10
        operator = random.choice(['+', '-', '*', '/'])
    elif score < 30:
        # Combine two operators after score 20
        operator1 = random.choice(['+', '-', '*', '/'])
        operator2 = random.choice(['+', '-', '*', '/'])
        operator = operator1 + operator2
    elif score < 50:
        # Combine three operators after score 30
        operator1 = random.choice(['+', '-', '*', '/'])
        operator2 = random.choice(['+', '-', '*', '/'])
        operator3 = random.choice(['+', '-', '*', '/'])
        operator = operator1 + operator2 + operator3
    else:
        # Use all four operators after score 50
        operator1 = random.choice(['+', '-', '*', '/'])
        operator2 = random.choice(['+', '-', '*', '/'])
        operator3 = random.choice(['+', '-', '*', '/'])
        operator4 = random.choice(['+', '-', '*', '/'])
        operator = operator1 + operator2 + operator3 + operator4

    result = calculate(operator, num1, num2)

    # Check if the result is a whole number
    if result.is_integer():
        result = int(result)
    else:
        result = int(result) + 1

    print("What is the calculation to get", result, "using the operator", operator, "?")

    # Get the user's calculation and check if it's correct
    calculation = input()

    if "+0" in calculation or "-0" in calculation:
        print("Please input a different calculation.")
        continue

    if "/1" in calculation and operator == '/':
        print("Please input a different calculation. Try again.")
        continue

    if "*1" in calculation and operator == '*':
        print("Please input a different calculation. Try again.")
        continue

    if eval(calculation) == result:

        score += 1
        print("""Correct
Your score =""", score)
    else:
        print("Game over")
        print("Your final score is", score)
        break
