str1 = "Hello world"
print(str1.count("o"))







number1 = int(input("Enter number1 "))
number2 = int(input("Enter number2 "))

print(f'Result of {number1} + {number2} = {number1 + number2}')
print(f'Result of {number1} - {number2} = {number1 - number2}')
print(f'Result of {number1} * {number2} = {number1 * number2}')
print(f'Result of {number1} / {number2} = {number1 / number2}')

# % means modulus (Reminder)
print(f'Result of {number1} % {number2} = {number1 % number2}')

# ** means Exponent
print(f'Result of {number1} ** {number2} = {number1 ** number2}')

# // means integer division
print(f'Result of {number1} // {number2} = {number1 // number2}')







first_name = input("What is your first name? ")
last_name = input("What is you last name? ")
year_of_birth = int(input("What is your year of birth? "))
address = input("What is your address? ")
zip_code = input("What is your zip code? ")
age = 2020 - year_of_birth
print(f"""Name: {first_name} {last_name}
Age: {age}
address: {address}
zip code: {zip_code}""")