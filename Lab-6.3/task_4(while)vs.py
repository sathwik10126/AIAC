def sum_n(n):
    s = 0  
    while n > 0:
        s += n  
        n -= 1 
    return s

n = int(input("Enter a number: "))
result = sum_n(n)
print("The sum of n natural numbers is", result)