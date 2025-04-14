# hunt treasure

row1 = ["A", "B", "C", "D"]
row2 = ["E", "F", "G", "H"]
row3 = ["I", "J", "K", "L"]
row4 = ["M", "N", "O", "P"]

treasureArea = [row1, row2, row3, row4]

treasureValues = [
    ["Gold Coin", None, "Ruby", None],
    [None, "Silver Key", None, None],
    [None, "Emerald", None, None],
    [None, None, "Magic Scroll", None],
]

print("\n", row1, "\n", row2, "\n", row3, "\n", row4)
position = input("Enter a treasure location: ")

treasureFound = None

for row in range(4):
    for col in range(4):
        if treasureArea[row][col].lower() == position.lower():
            treasureFound = treasureValues[row][col]
            break

    if treasureFound:
        break

if treasureFound == None:
    print("SORRY!! No treasure ")
else:
    print(f"hurray!! you found a {treasureFound}")
