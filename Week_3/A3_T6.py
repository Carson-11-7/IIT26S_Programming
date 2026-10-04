METERS_IN_KM = 1000.0
GRAMS_IN_POUND = 453.6

print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")
print()
print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice = int(input("Your choice: "))

if choice == 1:
    print()
    print("Length options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    length_choice = int(input("Your choice: "))

    if length_choice == 1:
        meters = float(input("Insert meters: "))
        kilometers = meters / METERS_IN_KM
        print(f"{meters:.1f} m is {kilometers:.1f} km")
    elif length_choice == 2:
        kilometers = float(input("Insert kilometers: "))
        meters = kilometers * METERS_IN_KM
        print(f"{kilometers:.1f} km is {meters:.1f} m")
    elif length_choice == 0:
        print("Exiting...")
    else:
        print("Unknown option.")

elif choice == 2:
    print()
    print("Weight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    weight_choice = int(input("Your choice: "))

    if weight_choice == 1:
        grams = float(input("Insert grams: "))
        pounds = grams / GRAMS_IN_POUND
        print(f"{grams:.1f} g is {pounds:.1f} lb")
    elif weight_choice == 2:
        pounds = float(input("Insert pounds: "))
        grams = pounds * GRAMS_IN_POUND
        print(f"{pounds:.1f} lb is {grams:.1f} g")
    elif weight_choice == 0:
        print("Exiting...")
    else:
        print("Unknown option.")

elif choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print()
print("Program ending.")