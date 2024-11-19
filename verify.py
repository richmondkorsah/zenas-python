# Create a program that asks for the user’s age. Print "You are a minor" if the age is below 18, otherwise print "You are an adult."

def verify(age):
    if age > 18:
        return "You are an adult"
    else:
        return "You are a minor"
        
age = int(input("Enter your age: "))

print(f"You are {age} years old. {verify(age)}.")