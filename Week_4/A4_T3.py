print("Program starting.")
print()
start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))
print()
print("Starting while-loop:")

current = start  
result = ""     
while current <= stop:
    result += str(current)
    if current < stop:
        result += " "
    current += 1
print(result)


print()
print("Program ending.")
    
