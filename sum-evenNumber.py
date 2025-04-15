number = int(input("Enter a number upto which you want sum of even numbers: "))

sum = 0
for num in range(0, number + 1, 2):
    sum += num

print(f"The sum is {sum}")
