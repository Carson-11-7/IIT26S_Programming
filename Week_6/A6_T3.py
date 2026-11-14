def read_write():
    filename = input("Insert source file name: ")
    file = open(filename, 'r')
    content = ""
    while True:
        line = file.readline()
        if len(line)==0:
            break
        content += line
    file.close()
    Dfilename = input("Insert destination file name: ")
    
    print(f"Reading file '{filename}' content.")
    print("File content ready in memory.")
    print(f"Writing content into file '{Dfilename}'.")
        
    Wfile = open(Dfilename, "w")
    Wfile.write(content)
    Wfile.close()


def main():
    print("Program starting.")
    print("This program can copy a file.")
    read_write()
    print("Copying operation complete.")
    print("Program ending.") 


main()