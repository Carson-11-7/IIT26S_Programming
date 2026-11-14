SEPARATOR = ";"


def readValues(filename):
    values: str = ""
    file = open(filename, "r")
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        line = line.strip()
        if len(line) > 0:
            values += line + SEPARATOR
    file.close()
    return values


def analyseValues(values):
    total = 0
    count = 0
    greatest = 0

    for item in values.split(SEPARATOR):
        if len(item) > 0:
            number = int(item)
            total += number
            count += 1
            if count == 1 or number > greatest:
                greatest = number

    average = 0
    if count > 0:
        average = total / count

    return ("Count;Sum;Greatest;Average\n"
        + str(count) + SEPARATOR + str(total) + SEPARATOR
        + str(greatest) + SEPARATOR + "{:.2f}".format(average)
        + "\n")


def displayResults(filename: str, results: str):
    print("#### Number analysis - START ####")
    print('File "' + filename + '" results:')
    print("Count;Sum;Greatest;Average")
    print(results)
    print()
    print("#### Number analysis - END ####")


def main():
    print("Program starting.")
    filename = input("Insert filename: ")
    values = readValues(filename)
    results = analyseValues(values)
    displayResults(filename, results)
    print("Program ending.")


if __name__ == "__main__":
    main()