LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PLACES = ["home", "Galba's palace", "Otho's palace",
          "Vitellius' palace", "Vespasian's palace"]


def rot13(text):
    result = ""
    for char in text:
        if char in LOWER:
            result += LOWER[(LOWER.find(char) + 13) % 26]
        elif char in UPPER:
            result += UPPER[(UPPER.find(char) + 13) % 26]
        else:
            result += char
    return result


print("Travel starting.")


file = open("player_progress.txt", "a")
file.close()


file = open("player_progress.txt", "r")
row = ""
while True:
    line = file.readline()
    if len(line) == 0:
        break
    if len(line.strip()) > 0:
        row = line.strip()
file.close()

if row == "":
    file = open("player_progress.txt", "w")
    file.write("current_location;next_location;passphrase\n0;1;qvfpvcyvar\n")
    file.close()
    row = "0;1;qvfpvcyvar"

current, nxt, cipher_pass = row.split(";")
plain_pass = rot13(cipher_pass)

print("Currently at " + PLACES[int(current)] + ".")
print("Travelling to " + PLACES[int(nxt)] + "...")
print("...Arriving to the " + PLACES[int(nxt)] + ".")
print("Passing the guard at the entrance.")
print('"' + plain_pass.capitalize() + '!"')
print("Looking for the message in the palace...")

file = open(nxt + "_" + cipher_pass + ".gkg", "r")
first_line = file.readline().strip()
rest = file.read()
file.close()
print("Ah, there it is! Seems cryptic.")

file = open("player_progress.txt", "a")
file.write(first_line + "\n")
file.close()
print("[Game] Progress autosaved!")

print("Deciphering Emperor's message...")
file = open(nxt + "-" + plain_pass + ".txt", "w")
file.write(rot13(rest))
file.close()
print("Looks like I've got now the plain version copy of the Emperor's message.")

print("Time to leave...")
print("Travel ending.")