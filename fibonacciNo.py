#print fibonacci terms f(n) = f(n-1) + f(n-2)

n = int(input("Enter the number :"))
def fibonacci(n):
    if ( n == 0 ):
        return 0
    elif ( n == 1 ):
        return 1
    elif (n < 0 ):
        print("Can't evaluate due to Negative Integer")
    else :
        return fibonacci(n-1) + fibonacci(n-2)
fibo = []

for i in range(0,n):
    fibonacci(i)
    fibo.append(fibonacci(i))

print(f"The {n}th Fibonacci Number is {fibonacci(n-1)}")
print(f"THe full Fibonacci series is = {fibo[::]}")
    