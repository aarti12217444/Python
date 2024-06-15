#WAP in which u have to take input from user in integer form and print the week name other than print invalid input.


a=int(input("Enter a: "))
if(a == 1):
    print("Monday")
elif(a == 2):
    print("Tuesday")
elif( a == 3):
    print("Wednesday")
elif(a == 4):
    print("Thrusday")
elif(a == 5):
    print("Friday")
elif(a == 6):
    print("Saturady")
elif(a == 7):
    print("Sunday")
else:
    print("Invalid input. Please enter correct input")


#wap in which u have to take input from user in string form and print instruction according to traffic ligh.

light = input("Enter light color: ")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("Light is broken")

#wap to take input from user and make a grading system.

marks = int(input("Enter marks: "))
if marks >= 90:
    print("O Grade")
elif (marks >= 80):
    print("A+ Grade")
elif (marks >= 70):
    print("B+ Grade")
elif (marks >= 60):
    print("B Grade")
elif (marks >= 50):
    print("C+ Grade")
elif (marks >= 40):
    print("D Grade")
else:
    print("E Grade")


#wap to make a simple calculator in which u have to take three input from user 2 in is form of integer and 3rd in in condition

a = int(input("Enter a: "))
b = int(input("Enter b: "))
n = int(input("Enter condition (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division): "))

if n == 1:
    print("Addition: ", a + b)
elif n == 2:
    print("Subtraction: ", a - b)
elif n == 3:
    print("Multiplication: ", a * b)
elif n == 4:
    print("Division: ", a / b)
else:
    print("Invalid selection. Please select a number between 1 and 4.")

    
