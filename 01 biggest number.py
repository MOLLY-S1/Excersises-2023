"""Input two numbers and output the bigger one or message saying
they are equal
"""

num1 = int(input("Number 1:"))
num2 = int(input("number 2:"))

while num1 != 0 or num2 != 0:
    if num1 > num2:
        print(num1)
    elif num2 == num1:
        print("they are equal")
    else:
        print(num2)

    num1 = int(input("Number 1:"))
    num2 = int(input("number 2:"))
