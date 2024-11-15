def addition(x,y):    
    return x + y

def subtraction(x,y):
    print("Your difference is: ")
    return x-y

def multiplication(x,y):
    print("Your product is: ")
    return x * y

def division(x,y):
    if y != 0:
        print("Error!! Division by zero")
    else:
        print("Your divisor is: ")
        return x // y


print("######################")
print(" A Simple Calculator ")
print("######################\n")

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

print("")
print("Select choice: ")
print("   [1] => Addition")
print("   [2] => Subtraction")
print("   [3] => Multiplication")
print("   [4] => Division\n")

choice = int(input("Enter choice: "))

if choice == 1:
    addition(num1,num2)
elif choice == 2:
    subtraction(num1,num2)
elif choice == 3:
    multiplication(num1,num2)
elif choice == 4:
    division(num1,num2)
else:
    print("Invalid input")









