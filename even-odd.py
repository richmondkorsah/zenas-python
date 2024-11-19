# Write a program that takes a number from the user and prints whether it is odd or even.

def even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

number = int(input("Enter a number: "))
print(f"Your number {number} is {even_odd(number)}")