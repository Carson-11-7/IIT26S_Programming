LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Program starting.")
print()
print("Collecting plain text rows for ciphering.")

rows = []
while True:
    row = input("Insert row(empty stops): ")
    if len(row) == 0:
        break
    rows.append(row)
    
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

print()
print("#### Ciphered text ####")
for row in ciphered_rows:
    print(row)
print()
print("#### Ciphered text ####")

filename = input("Insert filename to save: ")
file = open(filename, "w")
for row in ciphered_rows:
    file.write(row + "\n")
file.close()
print("Ciphered text saved!")
print("Program ending.")