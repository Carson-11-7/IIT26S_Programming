<<<<<<< HEAD
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
=======
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
>>>>>>> 29dcc5788fdb6dbfe94958ed4ea69475a7d44ef5
print("Program ending.")