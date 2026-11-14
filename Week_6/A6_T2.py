
def write(firstname, lastname, filename):
    file = open(filename, "w")
    file.write(firstname + '\n')
    file.write(lastname + '\n')
    file.write("")
    file.close()
    return None

def main():
    print("Program starting.")
    firstname = input("Insert first name:")
    lastname = input("Insert last name:")
    filename = input("Insert file name:")
    write(firstname, lastname, filename)
    print("Program ending.")
    return None

main()