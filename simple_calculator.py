# Calculator

def add(a,b):
    return a+b


def subtract(a,b):
    return a-b

def divide(a,b):
    return a/b

def multiplication(a,b):
    return a*b
print("Select operation \n 1:add\n 2:substract\n 3:divide\n 4:multiplication")
choice = int(input("Enter value: "))

a = float(input("Enter 1st value:"))
b = float(input("Enter 2nd value:"))


if choice == 1:
    print(a,"+", b,"=",add(a, b))
    
if choice == 2:
    print(a,"-", b,"=",subtract(a, b))
    

if choice == 3:
    
    print(a,"/", b,"=",divide(a, b))
    
if choice == 4:
    print(a,"*", b,"=",multiplication(a, b))