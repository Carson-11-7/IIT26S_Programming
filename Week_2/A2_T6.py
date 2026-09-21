print('Program starting.')
print()
Hex=input('Insert a hex color: ')
print()
print('Colors')
red = Hex[1:3] # Always remember 1-2-3 is for example: FFA500 is the letter "F" not "A", Do not count the end.
green = Hex[3:5] # We are not counting in the number 1 as it's the "#"
blue = Hex[5:7]
print(f"- Red {red}")
print(f"- Green {green}")
print(f"- Blue {blue}")
print()
print('Program ending.')