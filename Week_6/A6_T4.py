print("Program starting.")
print("This program analyses a list of names from a file.")
filename = input("Insert file name to read: ")
print("Reading names from '" + filename + "'." )
print("Analysing names...")
print("Analysis complete!")

print("#### REPORT BEGIN ####")

file = open(filename, 'r')
names = []
while True:
    line = file.readline()
    if len(line)==0:
        break
    line = line.strip()
    if len(line) > 0:
        names.append(line)
file.close()

number_of_names = len(names)
longest_name = names[0]
shortest_name = names[0]
total = 0

for name in names:
    len(names)
    if len(name) > len(longest_name):
        longest_name = name
    if len(name) < len(shortest_name):
        shortest_name = name
    total += len(name)

print("Analysis complete!")

print("#### REPORT BEGIN ####")
print(f"Name count - {number_of_names}")
print(f"Shortest name - {len(shortest_name)} chars")
print(f"Longest name - {len(longest_name)} chars")
print(f"Average name - {total / number_of_names:.2f} chars")
print("#### REPORT END ####")
print("Program ending.")