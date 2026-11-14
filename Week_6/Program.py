LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def input_row() -> list:
    rows = []
    while True:
        row = input("Insert row(empty stops): ")
        if len(row) == 0:
            break
        rows.append(row)
    return rows


def cipher(rows) -> list:
    ciphered_rows = []
    for row in rows:
        ciphered = ""
        for char in row:
            if char in LOWER_ALPHABETS:
                ciphered += LOWER_ALPHABETS[(LOWER_ALPHABETS.find(char) + 13) % 26]
            elif char in UPPER_ALPHABETS:
                ciphered += UPPER_ALPHABETS[(UPPER_ALPHABETS.find(char) + 13) % 26]
            else:
                ciphered += char
        ciphered_rows.append(ciphered)
    return ciphered_rows


def save(ciphered_mesasage):
    filename = input("Insert filename to save: ")
    file = open(filename, "w")
    for row in ciphered_message:
        file.write(row + "\n")
    file.close()


def main() -> None:
    print("Program starting.")
    print()
    #----------------------------------------------#
    print("Collecting plain text rows for ciphering.")
    input_row()
    save() 
    print()
    #----------------------------------------------#
    print("#### Ciphered text ####")
    lol = 
    print(lol)
    print()
    print("#### Ciphered text ####")
    #----------------------------------------------#
    save()
    print("Ciphered text saved!")
    print("Program ending.")

main()