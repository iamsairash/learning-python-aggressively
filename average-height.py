heights = input("Enter heights: ").split()

numberOfStudents = 0
avgHeight = 0
sumOfAllHeight = 0

print("list of heights are: ")
for height in heights:
    numberOfStudents += 1
    sumOfAllHeight += int(height)
    print(f"{height}", end=" ")

print()
avgHeight = sumOfAllHeight / numberOfStudents

print(f"The number of students: {numberOfStudents}")
print(f"The average height of students: {avgHeight:.2f}")
