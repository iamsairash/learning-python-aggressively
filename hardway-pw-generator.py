# here the pw will be generated randomly not in sequence like first letters, then symbol, and then numbers.

import random
import string

letters = list(string.ascii_lowercase + string.ascii_uppercase)

numbers = list(string.digits)

symbols = list("!@#$%^&*()_+-=[]{}|;:',<>.?/")

nr_letters = int(
    input("How many number of letters would you like to have in your password?: ")
)
nr_symbols = int(input("How many numbers of symbols would you like?: "))
nr_numbers = int(input("How many numbers of numbers would you like?: "))

password_list = []

for letter in range(0, nr_letters):
    password_list.append(random.choice(letters))

for symb in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for num in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)  # it shuffle the list items randomly

generated_password = ""

for letter in password_list:
    generated_password += letter

print(generated_password)
