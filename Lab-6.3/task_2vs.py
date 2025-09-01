def multiplication_table(n):
    i=1
    for i in range(1,11):
        b=n*i
        print(n,"*",i,"=",b)
n=int(input("enter a number:"))
multiplication_table(n)