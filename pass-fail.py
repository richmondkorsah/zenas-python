# Ask the user for their score (0-100) and print "Pass" if the score is 50 or above and "Fail" if it is below 50.

def pass_fail(marks, min, max):
    if min <= marks <= max and marks >= 50:
        return "Pass"
    else:
        return "Fail"
    
min = 0
max = 100

marks = int(input("Enter your marks: "))

print(f"You scored {marks}. It is a {pass_fail(marks, min, max)}.")