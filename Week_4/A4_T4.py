<<<<<<< HEAD
print("Program starting.")
print()

word_count = 0
character_count = 0
word = input("Insert word (empty stops): ")
while word != "":
    word_count += 1
    character_count += len(word)
    word = input("Insert word (empty stops): ")

print()
print("You inserted:")
if word_count <= 1:
    print("- ", word_count," word")
else:
    print("- ", word_count," words")
if character_count <= 1:
    print("- ", character_count," character")
else:
    print("- ", character_count," characters")

print()
=======
print("Program starting.")
print()

word_count = 0
character_count = 0
word = input("Insert word (empty stops): ")
while word != "":
    word_count += 1
    character_count += len(word)
    word = input("Insert word (empty stops): ")

print()
print("You inserted:")
if word_count <= 1:
    print("- ", word_count," word")
else:
    print("- ", word_count," words")
if character_count <= 1:
    print("- ", character_count," character")
else:
    print("- ", character_count," characters")

print()
>>>>>>> 29dcc5788fdb6dbfe94958ed4ea69475a7d44ef5
print("Program ending.")