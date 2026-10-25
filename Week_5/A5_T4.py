def askDimension(PPrompt: str) -> float:
    Feed = float(input(PPrompt))
    return Feed


def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    Result = PWidth * PHeight
    return Result


print("Program starting.")
Width = askDimension("Insert width: ")
Height = askDimension("Insert height: ")

Area = calcRectangleArea(Width, Height)
print()
print(f"Area is {Area}²")
print("Program ending.")
