def fizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzBuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


print(fizzBuzz(5))
