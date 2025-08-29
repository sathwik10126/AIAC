def sort_list(data):
    # Separate numbers and strings into different lists
    numbers = [item for item in data if isinstance(item, (int, float))]
    strings = [item for item in data if isinstance(item, str)]
    
    # Sort each list individually
    numbers.sort()
    strings.sort()
    
    # Combine the sorted lists (numbers first, then strings)
    return numbers + strings

# Example usage
items = [3, "apple", 1, "banana", 2]
print(sort_list(items))