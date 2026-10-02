#Take input from User 
#Do simple Operation 
#Print in Binary form 

print("Hello User, I am Binary converter")

num = int(input("Please enter the number you want to convert into Binary:\n"))

binary = []

def divisorFn(num, binary):
    result = num // 2
    remainder = num % 2

    binary.append(remainder)

    return result


while num > 0:
    num = divisorFn(num, binary)

print("".join(map(str, binary[::-1])))
    
    