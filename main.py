def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(f"Word count: {countWords(file_contents)}")
        print(f"Character count: {countCharacters(file_contents)}")

def countWords(text):
    return len(str(text).split())

def countCharacters(text):
    counts = {}
    for c in text:
        lowered = c.lower()
        counts[lowered] = counts.get(lowered, 0) + 1
    return counts

main()
