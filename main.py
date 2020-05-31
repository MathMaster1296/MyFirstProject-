#Class #3
done = "\nDone with Program. Proceeding to Next Program.\n\n\n"
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