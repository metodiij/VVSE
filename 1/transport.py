km = int(input("Enter km: "))
time = str(input("Enter time(d/n): "))
if km <= 20:
    print("Taxi is your only option")
    if time == "d":
        price = 0.79*km +0.70
    elif time == "n":
        price = 0.90*km +0.70
elif 20 < km <= 100:
    print("Bus is your better option")
    price = 0.09*km
elif 100 < km:
    print("Train is your best option")
    price = 0.06*km
print("Price = ", price)