# find the highest mark

marks = input("Enter the marks: ").split()

highestMark = 0

for mark in marks:
    if int(mark) > highestMark:
        highestMark = int(mark)

print(f"The highest mark is {highestMark}")
