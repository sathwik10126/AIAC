def multiplication_table(n):
    i=1
    while i<=10:
        b=n*i
        print(n,"*",i,"=",b)
        i=i+1
n=int(input("enter a number:"))
multiplication_table(n)
