numbers = []
count = int(input("Insert count: "))

text = input("Enter whole numbers separated by spaces: ")
for item in text.split():
    numbers.append(int(item))

def average(values):
    total = 0
    for n in values:
        total += n
    return total / len(values)

def describe(n):
    if n % 2 == 0:
        return "even"
    elif n > 10:
        return "odd and big"
    else:
        return "odd"

print("Average:", average(numbers))
print("Square of 4:", 4 ** 2, "| 17 // 5 =", 17 // 5, "| 6 * 7 =", 6 * 7)

for n in numbers:
    print(n, "is", describe(n))

while count > 0:
    print("Countdown:", count)
    count -= 1
print("Done!")