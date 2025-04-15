# print fizz-buzz when the nubmer is divisible of 3 and 5. fizz when divisible by 3 and buzz when divisible by 5.

number = int(input())

for num in range(1, number + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizz-buzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
