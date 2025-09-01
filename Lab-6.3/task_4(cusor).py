def sum_n(n):
    s=0
    for i in range(1, n+1):
        s=s+i
    return s

n=int(input("enter a number:"))
result=sum_n(n)
print("The sum of n natural numbers is", result)