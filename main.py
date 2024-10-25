def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(f"{num_words} words found in the document")
    print("----------------------------------------")
    print_letter_report(num_letters)

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
            if l.isalpha():
                letters[l] = 1
    return letters

def sort_on(dict):
    return dict["value"]

def print_letter_report(letterlist):
    letters = []
    for i in letterlist:
        letters.append({"key":i, "value": letterlist[i]})

    letters.sort(reverse=True, key=sort_on)
    for l in letters:
        print(f"The \'{l['key']}\' character was found {l['value']} times")
    return None

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()