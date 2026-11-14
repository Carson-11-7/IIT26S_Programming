LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def writeFile(Filename: str, Content: str):
    file = open(Filename, "w", encoding = "UTF-8")
    file.write(Content)
    file.close()


def askRows() -> str:
    rows = []
    while True:
        row = input("Insert row(empty stops): ")
        if len(row) == 0:
            break
        rows.append(row)
    return "\n".join(rows)


def shiftCharacter(Character: str, Alphabets: str, Shift: int = 13) -> str:
    position = Alphabets.find(Character)
    return Alphabets[(position + Shift) % len(Alphabets)]


def rot13(Content: str) -> str:
    result = ""
    for char in Content:
        if char in LOWER_ALPHABETS:
            result += shiftCharacter(char, LOWER_ALPHABETS)
        elif char in UPPER_ALPHABETS:
            result += shiftCharacter(char, UPPER_ALPHABETS)
        else:
            result += char
    return result


def main() -> None:
    print("Program starting.")
    print()
    print("Collecting plain text rows for ciphering.")

    message = askRows()
    ciphered = rot13(message)

    print()
    print("#### Ciphered text ####")
    print(ciphered)
    print()
    print("#### Ciphered text ####")

    filename = input("Insert filename to save: ")
    writeFile(filename, ciphered + "\n")

    print("Ciphered text saved!")
    print("Program ending.")


main()