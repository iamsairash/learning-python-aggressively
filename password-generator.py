import string
import random

# string.ascii_lowercase => "abcd........z"

# string.ascii_uppercase => "ABCD........Z"

# list("abcd") => ["a", "b", "c", "d"]

letters = list(string.ascii_lowercase + string.ascii_uppercase)

numbers = list(string.digits)

symbols = list("!@#$%^&*()_+-=[]{}|;:',.<>?/")

print("WELCOME TO THE PASSWORD GENERATOR: ")

nr_letters = int(input("How many letters would you like in your passwrod: "))
nr_symbols = int(input("How many symbols would you like: "))
nr_numbers = int(input("How many numbers would you like: "))

letters_generated = ""
numbers_generated = ""
symbol_generated = ""

for letter in range(0, nr_letters):
    l = letters[random.randint(0, len(letters) - 1)]
    letters_generated += l

for num in range(0, nr_numbers):
    n = numbers[random.randint(0, len(numbers) - 1)]
    numbers_generated += n

for symb in range(0, nr_symbols):
    s = symbols[random.randint(0, len(symbols) - 1)]
    symbol_generated += s

password_generated = letters_generated + numbers_generated + symbol_generated

print(password_generated)
