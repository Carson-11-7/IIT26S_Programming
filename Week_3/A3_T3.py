name = input("Insert username: ")

print("1 - Print welcome message")
print("2 - Exit")
choice = int(input("Your choice: "))

if choice == 1:
    print(f"Welcome {name}!")
elif choice == 2:
    print("Exiting...")
else:
    print("Unknown option.")
print()
print("Program ending.")