def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Get user input
try:
    user_score = float(input("Enter the score: "))
    print(f"The grade is: {grade(user_score)}")
except ValueError:
    print("Please enter a valid numeric score.")