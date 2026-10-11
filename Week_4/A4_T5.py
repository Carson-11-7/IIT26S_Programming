print("Program starting.")
print()
start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))
print()

skibidi = True

if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    skibidi = False

if inspection < start or inspection > stop:
    print("Inspection value must be within the range of start and stop.")
    skibidi = False

if skibidi:
    print("First loop - inspection with break:")
    result = ""
    for i in range(start, stop):
        if i == inspection:
            break
        result += str(i) + " "
    print(result.strip())

    print("Second loop - inspection with continue:")
    result = ""
    for i in range(start, stop):
        if i == inspection:
            continue
        result += str(i) + " "
    print(result.strip())

print()
print("Program ending.")