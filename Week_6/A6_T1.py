def read(filename):
    file = open(filename, 'r', encoding='UTF-8')
    while True:
        line = file.readline()
        if len(line)==0:
            break
        print(line, end ="")
    file.close()


def main():
    print("Program starting.")
    print("This program can read a file.")
    filename = input("Insert filename: ")
    print("#### START",f"{filename}","####")
    read(filename)
    print()
    print("#### END",f"{filename}","####")
    print("Program ending.")
    return None

main()