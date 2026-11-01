print("Program starting.")
print("This program can read a file.")
filename = input("Insert filename:")
file = open(filename, 'r')
print("#### START",f"{filename}","####")
while True:
    line = file.readline()
    if len(line)==0:
        break
    print(line, end ="")
file.close()
print()
print("#### END",f"{filename}","####")
print("Program ending.")