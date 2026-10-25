Word = ""
Choice = 6967

print("Program starting.")
while Choice != 0:
    print("Options:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")
    Choice = int(input("Your choice: "))

    if Choice == 1:
        Word = input("Insert word: ")
    elif Choice == 2:
        print(f'Current word - "{Word}"')
    elif Choice == 3:
        print(f'Word reversed - "{Word[::-1]}"')
    elif Choice == 0:
        print("Exiting program.")
    else:
        print("Unknown option! try again")
    print()
print("Program ending.")