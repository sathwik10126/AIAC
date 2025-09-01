def age_classification(age):
    if age<13:
        return "Child"
    elif age>=13 and age<20:
        return "Teenager"
    elif age>=20 and age<65:
        return "Adult"
    elif age>=65:
        return "Senior"
    else:
        return "Invalid age"
age =int(input("enter your age:"))
print("You are classified as:", age_classification(age))