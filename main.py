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
        counted_chars = countCharacters(file_contents)
        chars_sorted_by_freq = dict(sorted(counted_chars.items(), key=lambda item: item[1], reverse=True))
        reportCharacters(chars_sorted_by_freq)
        print("===== End of report =====")

def reportCharacters(charDict):
    for c in charDict:
        if str(c).isalpha():
            print(f"The character '{c}' was found {charDict[c]} times")

main()
