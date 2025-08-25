def validate_mobile(number):
    """Validates Indian mobile number (starts with 6,7,8,9 and has 10 digits)"""
    return number.isdigit() and len(number) == 10 and number[0] in '6789'

# Main program
print("Indian Mobile Number Validator")
print("Enter 'quit' to exit")

while True:
    mobile = input("Enter mobile number: ").strip()
    
    if mobile.lower() == 'quit':
        break
        
    if validate_mobile(mobile):
        print("✅ Valid Indian mobile number!")
    else:
        print("❌ Invalid mobile number!")
    
    print("-" * 30)

print("Thank you!")