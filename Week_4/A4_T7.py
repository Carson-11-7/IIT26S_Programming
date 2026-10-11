print("Program starting.")
print()
print("Check multiplicative persistence.")
n = int(input("Insert an integer: "))

steps = 0
while n >= 10:
    digits = str(n)
    product = 1
    for d in digits:
        product *= int(d)
    print(" * ".join(digits), "=", product)
    n = product
    steps += 1

print("No more steps.")
print()
print("This program took", steps, "step(s)")
print()
print("Program ending.")