done = "\nDone with Program. Proceeding to Next Program.\n\n\n"
#Class #4




number = int(input("Enter a number: "))
prime = "The number is prime."
for x in range(2, number):
  if number % x == 0:
    prime = "The number is composite."
    break
print(prime)
print(done)



number = int(input("Enter a number: "))
number1 = 0
number2 = 1
if number <= 0:
  print("Invalid Input.")
elif number == 1:
  print(number1)
else:
  print(number1)
  print(number2)
  for x in range(number - 2):
    print(number1 + number2)
    number2 += number1
    number1 = number2 - number1
print(done)



number = int(input("Enter a number: "))
for x in range(1, number + 1):
  if x % 2 != 0 and x % 3 != 0:
    print(x)
print(done)



while True:
  number = int(input("Enter a number for Fizz Buzz! (Or type 0 for quit): "))
  if number == 0:
    break
  if number % 15 == 0:
    print("Fizz Buzz!")
  elif number % 5 == 0:
    print("Buzz!")
  elif number % 3 == 0:
    print("Fizz!")
  else:
    print("Oops!")
print(done)



factorial_number = int(input("Enter a number: "))
factorial = 1
for d in range(2, factorial_number + 1):
  factorial *= d
print(f"The factorial of {factorial_number} is {factorial}")
print(done)



#Class #3
b = "nothing"
c = "nothing"
while not(b == "quit"):
  b = input("Do you want to turn the fan on, off, or quit?: ")
  if b == "on" or b == "off":
    if (b == c):
      print(f"Fan is already {b}")
    else: 
      print(f"Fan turned {b}")
  elif not(b == "quit"):
    print("Invalid Input. Please Try Again.")
  c = b
print(done)



num = int(input("Enter a Number: "))
if num % 2 == 1:
  print("The number is odd.")
else:
  print("The number is even.")
print(done)



z = int(input("Enter a number: "))
for a in range(z + 1):
  print(a)
print(done)


text = input("What text do you want? ")
number = 1
for number1 in text:
  print(f"{number} -> {number1}")
  number += 1
print(done)


weightunit = input("Weight Unit: ")
weight = int(input("Weight: "))
if weightunit.lower() == "kg":
  print(f"about {weight*2.2//1} pounds")
elif weightunit.lower() == "lb":
  print(f"about {weight//2.2} kilograms")
else:
  print("Invalid")
print(done)


age = int(input("What is your child's age? "))
if age <= 0:
  print("not born")
elif 0 < age <= 3:
  print("toddler")
elif 3 < age <= 12:
  print("child")
elif 12 < age <= 18:
  print("teenager")
else:
  print("adult")
print(done)


x = int(input("First number: "))
y = int(input("Second number: "))
if x > y:
  print(f"{x} - {y} = {x - y}")
elif x < y:
  print(f"{y} - {x} = {y - x}")
else:
  print("They are both equal")
print("Done with all Programs")