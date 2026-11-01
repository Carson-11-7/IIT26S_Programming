print("Program starting.")
print("This program can copy a file.")
filename = input("Insert source file name:")
Dfilename = input("Insert destination file name:")
print("Reading file ", f'{filename}', " content.")
print("File content ready in memory.")
file = open(filename, 'r')
content = ""
while True:
    line = file.readline()
    if len(line)==0:
        break
    content += line
file.close()

print("File content ready in memory.")

print("Writing content into file '" + Dfilename + "'.")
Wfile = open(Dfilename, "w")
Wfile.write(content)
Wfile.close()

print("Copying operation complete.")
print("Program ending.") 