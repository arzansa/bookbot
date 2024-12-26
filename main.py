import sys
def main():
    try:
        src = sys.argv[1]
    except:
        print("You've not provided an argument. Please provide the text file you'd like to analyze like so: python3 'books/frankenstein.txt'")
        quit()
    createReport(src)

def countWords(text):
    return len(str(text).split())

def countCharacters(text):
    counts = {}
    for c in text:
        lowered = c.lower()
        counts[lowered] = counts.get(lowered, 0) + 1
    return counts

def createReport(src):
    with open(src) as f:
        file_contents = f.read()
        print(f"===== Analyzing document {src} =====") 
        print(f"Word count: {countWords(file_contents)}")
        # print(f"Character count: {countCharacters(file_contents)}")
        # reportCharacters(sorted(countCharacters(file_contents).values()))
        reportCharacters(countCharacters(file_contents))

def reportCharacters(charDict):
    print(charDict)
    for c in charDict:
        # print(c)
        # print(type(c))
        # if str(charDict[c]).isalpha():
        print(f"The character {c} was found {charDict[c]} times")

main()
