print("Ishit's Pro calculator")

d = input("enter operation: ")

if(d == "add"):
  a = int(input("enter first number:"))
  b = int(input("enter second number:"))
  e = int(input("enter third number:"))
  c = a + b + e

  print("the sum is: ", c)

if(d == "divide"):

  a = int(input("enter dividend: "))
  b = int(input("enter divisor: "))

  c = a/b

  print("the quotent is",c)

if(d == "multiply"):
  a = int(input("enter first number:"))
  b = int(input("enter second number:"))

  c = a*b

  print("the product is: ", c)

if(d == "subtract"):
  a = int(input("enter first number:"))
  b = int(input("enter second number:"))
  e = int(input("enter third number:"))

  c = a - b - e

  print("the difference is: ", c)

if(d == "power"):
  a = int(input("enter first number:"))
  b = int(input("enter second number:"))

  c = a**b

  print("the answer is: ", c)
if(d == "remainder"):
  a = int(input("enter first number:"))
  b = int(input("enter second number:"))

  c = a%b

  print("the remainder is: ", c)

if(d == "percentage"):
  a = int(input("enter value:"))
  b = int(input("enter maximum value number:"))

  c = a*100/b

  print("the percentage is: ", c)

if(d == "test"):
  print("hello world")
  print("test successful")

if(d == "compare"):
  a= int(input("enter first number: "))
  b= int(input("enter second number: ")) 

  if( a > b):
    print("Value 1 is greater")
  if(a < b):
    print("Value 2 is greater")
  if(a := b):
   print("they both are equal")

if(d == "distance converter"):
  a = int(input("enter distance is kilometers: "))

  g = a/1.6

  print("the distance in miles is: ",g)

input("Press Enter to exit")








