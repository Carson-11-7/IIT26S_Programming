print("Program starting.")
n = int(input("Insert a positive integer: "))

steps = 0
result = str(n)

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    steps += 1
    result += " -> " + str(n)

print(result)
print("Sequence had", steps, "total steps.")

print()
print("Program ending.")