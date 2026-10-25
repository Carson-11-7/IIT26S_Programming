def showOptions() -> None:
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")

def askChoice() -> int:
    Feed = input("Your choice: ")
    if Feed.isnumeric():
        return int(Feed)
    return -1

def main() -> None:
    Count = 0
    Choice = 67

    print("Program starting.")
    while Choice != 0:
        showOptions()
        Choice = askChoice()

        if Choice == 1:
            print(f"Current count - {Count}")
        elif Choice == 2:
            Count += 1
            print("Count increased!")
        elif Choice == 3:
            Count = 0
            print("Cleared count!")
        elif Choice == 0:
            print("Exiting program.")
        else:
            print("Unknown option!")
        print()
    print("Program ending.")

main()