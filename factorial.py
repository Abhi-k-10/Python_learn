#factorial calculator 
n = int(input("Enter the number whos factorial is required  : "))
def factorial(n):
    if (n == 0 or n == 1 ):
        return 1
    else :
        return n * factorial(n-1)


print(factorial(n))