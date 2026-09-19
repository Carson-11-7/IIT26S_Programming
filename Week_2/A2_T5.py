print('Program starting.')
print()
word = input("Insert a closed compound word: ")
print(f"The word you inserted is '{word}' and in reverse it is '{word[::-1]}'.")
# The [::-1] is simply the slicing function [start:end:step].
#  - start is left empty means py will automatically runs the list from the start.
#  - end is also left empty means py will runs the list to the end.
#  - step = -1 means to move backward by one character each time.
print(f"The inserted word length is {len(word)}")
print(f"Last character is '{word[-1]}'")
#   Word[i] is to take one character at the position i.
#   In this case i is -1. But why -1? if the word is Bananamoon for example.
#   The word has 10 characters each py counts from 0 to 9 in the normal way (py starts form 0 not 1).
#   And -1 to -10 in the reverse way like this: [-1]--> n o o m a n a n a B <--[-10].
print()
print("Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))
print()
substring = word[start:end:step] #this is a slicing func.
#  If your start input is 0 it's the first letter of the word.
#  And for example the word "hello" your end input is 3 so py will take the letter before the third letter "l", which is "e".
print(f"The word '{word}' sliced to the defined substring is'{substring}'.")
print('Program ending.')
