import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Thank you for using a secure password generator.")

num_letters = int(input("Please input the # of letters you want: "))
num_nums = int(input("Please input the # of numbers you want: "))
num_symbols = int(input("Please input the # of symbols you want:"))

passlist = []

for char in range(1, num_letters + 1):
    passlist += random.choice(letters)

for char in range(1, num_nums + 1):
    passlist += random.choice(numbers)

for char in range(1, num_symbols + 1):
    passlist += random.choice(symbols)

random.shuffle(passlist)

password = ""
for char in passlist:
    password += char

passwd = ''.join(passlist)

print(f"Your password is: {passwd}\nThank you for using this service!")