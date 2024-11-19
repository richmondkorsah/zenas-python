# Ask the user to input two numbers. Print "The first number is greater" if the first number is larger, "The second number is greater" if the second is larger, or "Both numbers are equal" if they are the same.

def num_compare(num1, num2):
    if num1 > num2:
        return f"{num1} is greater than {num2}"
    elif num2 > num1:
        return f"{num2} is greater than {num1}"
    

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print(num_compare(num1, num2))
except ValueError:
    print("Invalid number. Try again next time")