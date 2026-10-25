DELIMITER = ","

def collectWords() -> str:
    Words = ""
    while True:
        Word = input("Insert word(empty stops): ")
        if Word == "":
            break
        if Words == "":
            Words = Word
        else:
            Words = Words + DELIMITER + Word
    return Words

def analyseWords(PWords: str) -> None:
    WordList = PWords.split(DELIMITER)
    WordCount = len(WordList)
    CharCount = 0
    for Word in WordList:
        CharCount += len(Word)
    Avg = CharCount / WordCount

    print(f"- {WordCount} Words")
    print(f"- {CharCount} Characters")
    print("- {:.2f} Average word length".format(Avg))

def main() -> None:
    print("Program starting.")
    Collected = collectWords()
    analyseWords(Collected)
    print("Program ending.")

main()