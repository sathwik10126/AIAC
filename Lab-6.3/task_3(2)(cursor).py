def age_classification(age):
    match age:
        case _ if age<13:
            return "Child"
        case _ if 13<=age<20:
            return "Teenager"
        case _ if 20<=age<65:
            return "Adult"
        case _ if age>=65:
            return "Senior"
        case _:
            return "Invalid age"
age =int(input("enter your age:"))
print("You are classified as:", age_classification(age))