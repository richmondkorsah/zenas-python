# Ask the user for their score out of 100. Use conditions to print a grade based on the score:
    #  - 90 and above: "A"
    #  - 80-89: "B"
    #  - 70-79: "C"
    #  - 60-69: "D"
    #  - Below 60: "F"

def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'Fail'

def grade_calculator():
    print("Grade Calculator")
    try:
        score = float(input("Enter the score (0-100): "))
        if 0 <= score <= 100:
            grade = calculate_grade(score)
            print(f"The grade for a score of {score} is: {grade}")
        else:
            print("Invalid score! Please enter a value between 0 and 100.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

Add assignment files
grade_calculator()
