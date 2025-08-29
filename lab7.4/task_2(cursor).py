def sort_list(data):
    # Separate numbers and strings
    numbers = [x for x in data if isinstance(x, (int, float))]
    strings = [x for x in data if isinstance(x, str)]
    
    # Sort each type separately
    sorted_numbers = sorted(numbers)
    sorted_strings = sorted(strings)
    
    # Return combined sorted list (numbers first, then strings)
    return sorted_numbers + sorted_strings

# Test with mixed data types
items = [3, "apple", 1, "banana", 2]
print("Original list:", items)
print("Sorted list:", sort_list(items))

# Test with only numbers
numbers_only = [5, 2, 8, 1, 9]
print("\nNumbers only - Original:", numbers_only)
print("Numbers only - Sorted:", sort_list(numbers_only))

# Test with only strings
strings_only = ["zebra", "apple", "banana", "cherry"]
print("\nStrings only - Original:", strings_only)
print("Strings only - Sorted:", sort_list(strings_only))

