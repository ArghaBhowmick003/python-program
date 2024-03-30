print("Travel from City A to City B")
Time = int(input("Enter time: "))
Longer = int(input("Define longer(in hrs): "))
if (Time >= Longer):
    Price = int(input("Enter Price(in rupees): "))
    Higher = int(input("Define higher: "))
    if (Price >= Higher):
        print('Train')
    else:
        print('Coach')
else:
    Price = int(input("Enter Price(in rupees): "))
    Higher = int(input("Define higher: "))
    if (Price >= Higher):
        print('Daytime flight')
    else:
        print('Red Eye Flight')
print("Arrive City B")
