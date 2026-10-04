print("Program starting.")
print("Insert two integers.")
first = int(input("Insert first integer: "))
second = int(input("Insert second integer: "))

print("Comparing inserted integers.")
if first > second:
    print("First integer is greater.")
elif second > first:
    print("Second integer is greater.")
else:
    print("Integers are the same.")

print()
print("Adding integers together")
total = first + second
print(f"{first} + {second} = {total}")

print()
print("Checking the parity of the sum...")
if total % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")
print()
print("Program ending.")