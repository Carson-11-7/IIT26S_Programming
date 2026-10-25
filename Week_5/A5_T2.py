def frameWord(PWord):
    width = len(PWord) + 4
    print("*" * width)
    print(f"* {PWord} *")
    print("*" * width)
    
    return None

def main():
    print("Program starting.")
    PWord = input("Insert word:")
    print()
    frameWord(PWord)
    print()
    print("Program ending.")
    return None

main()