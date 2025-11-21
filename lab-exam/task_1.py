"""
Ride-Sharing ETA Sorting – With Automated Test Cases
Output Format: Matches the sample provided by the user
"""

# ---------------------------------------------------
# MERGE SORT
# ---------------------------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ---------------------------------------------------
# QUICK SORT
# ---------------------------------------------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid  = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)


# ---------------------------------------------------
# FUNCTION TO PROCESS
# ---------------------------------------------------
def sort_etas(etas, algorithm):
    return merge_sort(etas) if algorithm == "merge" else quick_sort(etas)


# ---------------------------------------------------
# AUTOMATED TEST CASES
# ---------------------------------------------------
def run_tests():
    print("==============================")
    print("      AUTOMATED TEST CASES")
    print("==============================\n")

    # ---------------- TEST CASE 1 ----------------
    test1_input = [12, 5, 7, 3, 18]
    expected1 = [3, 5, 7, 12, 18]
    actual1 = sort_etas(test1_input, "merge")

    print("TEST CASE 1")
    print("Input:")
    print(test1_input)
    print("Expected Output:", expected1)
    print("Actual Output:", actual1)
    print("STATUS:", "PASS" if actual1 == expected1 else "FAIL")
    print("\n----------------------------------\n")

    # ---------------- TEST CASE 2 ----------------
    test2_input = [25, 10, 40, 8, 15, 2]
    expected2 = [2, 8, 10, 15, 25, 40]
    actual2 = sort_etas(test2_input, "quick")

    print("TEST CASE 2")
    print("Input:")
    print(test2_input)
    print("Expected Output:", expected2)
    print("Actual Output:", actual2)
    print("STATUS:", "PASS" if actual2 == expected2 else "FAIL")
    print("\n----------------------------------\n")

    # ---------------- TEST CASE 3 ----------------
    test3_input = [6, 6, 3, 9, 1, 1, 8]
    expected3 = [1, 1, 3, 6, 6, 8, 9]
    actual3 = sort_etas(test3_input, "merge")

    print("TEST CASE 3")
    print("Input:")
    print(test3_input)
    print("Expected Output:", expected3)
    print("Actual Output:", actual3)
    print("STATUS:", "PASS" if actual3 == expected3 else "FAIL")
    print("\n----------------------------------\n")


# ---------------------------------------------------
# FINAL MAIN EXECUTION
# ---------------------------------------------------
if __name__ == "__main__":

    # Run automated tests
    run_tests()

    # Final actual program output (like your sample)
    print("Ride-Sharing ETA Results")
    print("--------------------------------------")

    etas = [12, 5, 7, 3, 18]
    sorted_etas = sort_etas(etas, "merge")
    fastest = sorted_etas[0]

    print(f"Fastest ETA: {fastest} minutes")
    print("Fully Sorted ETA List:", sorted_etas)
