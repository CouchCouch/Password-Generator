import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
symbols = "`~!@#$%^&*()-_=+\|]}[{\"';:,.<>?//"
password = ""
print("Length of password?")
length = input()
for i in range(int(length)):
  if i%5 == 1:
    password += random.choice(symbols)
  elif i%4 == 1:
    password += random.choice(numbers)
  elif i%2 == 1:
    password += random.choice(alphabet)
  else:
    password += random.choice(alphabet)
print("Your password is: ", password)