# random person's name to pay food bill

import random

listOfNames = []

while True:
    name = input("Enter the name: (press d for done)")
    if name.lower() != "d":
        listOfNames.append(name)
    else: 
        break

index = random.randint(0,len(listOfNames))

print(f"The random person is {listOfNames[index-1]}")