def search_item(items, target):
    """
    Search for a target element in a list.

    Args:
        items (list): A list of elements to search in.
        target (any): The element to search for.

    Returns:
        bool: True if the target is found, False otherwise.
    """
    return target in items

# Example usage
items = [10, 20, 30, 40, 50]
target = 30
found = search_item(items, target)
print("Found" if found else "Not Found")