while True:
    d = input("enter operation: ")

    if d == "add":
        a = float(input("enter first number: "))
        b = float(input("enter second number: "))
        e = float(input("enter third number: "))
        c = a + b + e
        print("the sum is: ", c)

    elif d == "divide":
        a = float(input("enter dividend: "))
        b = float(input("enter divisor: "))
        c = a / b
        print("the quotient is", c)

    elif d == "multiply":
        a = float(input("enter first number: "))
        b = float(input("enter second number: "))
        c = a * b
        print("the product is: ", c)

    elif d == "subtract":
        a = float(input("enter first number: "))
        b = float(input("enter second number: "))
        e = float(input("enter third number: "))
        c = a - b - e
        print("the difference is: ", c)

    elif d == "power":
        a = float(input("enter base: "))
        b = float(input("enter exponent: "))
        c = a ** b
        print("the answer is: ", c)

    elif d == "remainder":
        a = float(input("enter dividend: "))
        b = float(input("enter divisor: "))
        c = a % b
        print("the remainder is: ", c)

    elif d == "percentage":
        a = float(input("enter value: "))
        b = float(input("enter maximum value number: "))
        c = (a * 100) / b
        print("the percentage is: ", c)

    elif d == "test":
        print("hello world")
        print("test successful")

    elif d == "compare":
        a = float(input("enter first number: "))
        b = float(input("enter second number: "))

        if a > b:
            print("Value 1 is greater")
        elif a < b:
            print("Value 2 is greater")
        else:
            print("They both are equal")

    elif d == "distance converter":
        a = float(input("enter distance in kilometers: "))
        g = a / 1.6
        print("the distance in miles is: ", g)

    shutdown = input("Do you want to shut down? (yes/no): ")
    if shutdown.lower() == "yes":
        break
