line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Enter a position: (A1/A2/A3/B1/B2/B3/C1/C2/C3): ")

letter = position[0]
abc = ["a", "b", "c"]
col = abc.index(letter.lower())
row = int(position[1])-1

map[row][col] = "X"

print("\n",line1,"\n",line2,"\n", line3)