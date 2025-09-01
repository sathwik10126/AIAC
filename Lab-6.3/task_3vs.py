def age_classification(age):
    if age < 13:
        return "Child"
    elif 13 <= age < 20:
        return "Teenager"
    elif 20 <= age < 65:
        return "Adult"
    else:
        return "Senior"
age = int(input("Enter your age: "))
print("You are classified as:", age_classification(age))