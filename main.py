def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(f"{num_words} words found in the document")
    print(f"{num_letters}")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    letters = {}
    for i in text:
        l = i.lower()
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()