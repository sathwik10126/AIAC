def Age_Classifies():
    while True:
        try:
            age = int(input("Enter age (or -1 to exit): "))
            if age == -1:
                print("Exiting...")
                break
            elif 0 <= age <= 12:
                print("Child")
            elif 13 <= age <= 19:
                print("Teen")
            elif 20 <= age <= 59:
                print("Adult")
            elif age >= 60:
                print("Senior")
            else:
                print("Invalid age. Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Example usage
Age_Classifies()
