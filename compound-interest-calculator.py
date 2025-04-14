# compound interest calculator

principle = 0
rate = 0
time = 0

while True: 
    principle = float(input("Enter principle amount: "))
    if(principle <= 0):
        print("principle can't be zero or less than zero")
    else:
        break

while rate <= 0:
    rate = float(input("Enter the rate: "))
    if(rate <= 0):
        print("rate can't be zero or less than zero")

while time <= 0:
    time = int(input("Enter the time: "))
    if(time <= 0):
        print("Time can't be zero or less than zero")

totalAmout = principle * pow(1 + rate/100, time)
print(f"After {time} year/s, the amount will be ${totalAmout:.2f} at {rate}% interest rate")