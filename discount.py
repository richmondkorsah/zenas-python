# Write a program that asks for the user’s age. If the age is below 12 or above 65, print "You are eligible for a discount." Otherwise, print "No discount available."

def discount(age):
    if age > 18 < 65:
        return "You are eligible for discount"
    else:
        return "No discount available" # Pay with your pension money
        
age = int(input("Enter your age: "))

print(f"You are {age} years old. {discount(age)}.")