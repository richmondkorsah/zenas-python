# Write a program that asks for the user’s age and country. If they’re at least 18 and the country is "Ghana," print "You can vote." Otherwise, print "You cannot vote."


def vote(age):
    if age > 18:
        return "You are eligible to vote"
    else:
        return "You are not eligible to vote"
    

age = int(input("Enter your age: "))

print(f"You are {age} years old. {vote(age)}.")