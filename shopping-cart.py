# shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food (press C or c for cancel and D or d for done.): ")
    
    if food.lower() == "c":
        foods.clear()
        prices.clear()
        print("You canceled the shopping")
        break
    elif food.lower() == "d":
        if len(foods) == 0:
            print("Please do some shopping..😃")
            continue
        else:
            break
        
    foods.append(food)
    price = float(input("Enter the price: $"))
    prices.append(price)

print("Shopping Cart is empty") if len(foods)==0 else print("-----Shopping Cart-----")

for food in foods:
    print(food, end=" ")
    
print("=====>>>>", end=" ")
for price in prices:
    print(price, end=" ")
    total += price

if len(foods)>0: print(f"The toal price is ${total}")