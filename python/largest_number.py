#A program which prompts the user to enter five numbers and prints the largest number
# prompts the user to enter the first five numbers:
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
number4 = int(input("Enter the fourth number: "))
number5 = int(input("Enter the fifth number: "))

#Checks the greatest number:
largest_number = number1

if number2 > largest_number:
    largest_number = number2

if number3 > largest_number:
    largest_number = number3

if number4 > largest_number:
    largest_number = number4

if number5 > largest_number:
    largest_number = number5
#outputs the results (largest number)
print("The largest number is: ", largest_number)



