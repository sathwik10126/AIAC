def get_student_info():
    """Get student information from user input"""
    print("Enter student information:")
    print("-" * 30)
    
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    branch = input("Branch: ").strip()
    
    while True:
        try:
            sgpa = float(input("SGPA: "))
            if 0 <= sgpa <= 10:
                break
            else:
                print("SGPA must be between 0 and 10. Please try again.")
        except ValueError:
            print("Please enter a valid number for SGPA.")
    
    return {
        'first_name': first_name,
        'last_name': last_name,
        'branch': branch,
        'sgpa': sgpa
    }

def display_student_info(student):
    """Display student information in structured format"""
    print("\nStudent Information:")
    print(" " * 30 + f"Full name: {student['first_name']} {student['last_name']}")
    print(" " * 30 + f"Branch: {student['branch']}")
    print(" " * 30 + f"SGPA: {student['sgpa']}")

def main():
    """Main program to run student information parser"""
    print("Student Information Parser")
    print("=" * 40)
    
    while True:
        # Get student information
        student = get_student_info()
        
        # Display student information
        display_student_info(student)
        
        # Ask if user wants to continue
        print("\n" + "-" * 40)
        continue_input = input("Do you want to enter another student? (yes/no): ").strip().lower()
        
        if continue_input not in ['yes', 'y', '1']:
            break
    
    print("\nThank you for using Student Information Parser!")

if __name__ == "__main__":
    main()