#Finds operations such as squares , squaroots , cubes etc
num = float(input("Enter the Number :"))
operation = input("Select an operation \n1.Square \n2.Squareroot \n3.Cube \n4.Cube root \n")
operationList = [ "1" , "2" , "3" , "4" ]
def mainFn(num , operation):
    if (operation == "1" or operation == "Square"):
        return num**2
    elif (operation == "2" or operation == "Squareroot"):
        return num**(1/2)
    elif (operation == "3" or operation == "Cube"):
        return num**3
    elif (operation == "4" or operation == "Cuberoot"):
        return num**(1/3)
    else :
        print("Error :")

def operationPrint(operation):
    if (operation == "1" or operation == "Square"):
        return 'Square'
    elif (operation == "2" or operation == "Squareroot"):
        return 'Squareroot'
    elif (operation == "3" or operation == "Cube"):
        return 'Cube'
    elif (operation == "4" or operation == "Cuberoot"):
        return 'Cuberoot'
    else :
        print("Invalid operation !")


if operation in operationList:
    print(f"The {operationPrint(operation)} of {num} is {mainFn(num,operation)}")
else :
    print("Invalid operation !")