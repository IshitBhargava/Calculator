print("Ishit's Pro calculator")

print("supported operations are add, subtract, multiply, divide, remainder, distance converter, percentage, test, compare and power")

d = input("enter operation: ")

if d == "add":
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
    e = float(input("enter third number: "))
    c = a + b + e
    print("the sum is: ", c)

if d == "divide":
    a = float(input("enter dividend: "))
    b = float(input("enter divisor: "))
    c = a / b
    print("the quotient is", c)

if d == "multiply":
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
    c = a * b
    print("the product is: ", c)

if d == "subtract":
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
    e = float(input("enter third number: "))
    c = a - b - e
    print("the difference is: ", c)

if d == "power":
    a = float(input("enter base: "))
    b = float(input("enter exponent: "))
    c = a ** b
    print("the answer is: ", c)

if d == "remainder":
    a = float(input("enter dividend: "))
    b = float(input("enter divisor: "))
    c = a % b
    print("the remainder is: ", c)

if d == "percentage":
    a = float(input("enter value: "))
    b = float(input("enter maximum value number: "))
    c = (a * 100) / b
    print("the percentage is: ", c)

if d == "test":
    print("hello world")
    print("test successful")

if d == "compare":
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))

    if a > b:
        print("Value 1 is greater")
    elif a < b:
        print("Value 2 is greater")
    else:
        print("They both are equal")

if d == "distance converter":
    a = float(input("enter distance in kilometers: "))
    g = a / 1.6
    print("the distance in miles is: ", g)

input("Press Enter to exit")
