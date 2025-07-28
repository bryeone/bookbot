from stats import get_word_count
from stats import get_book_text
from stats import get_book_dictionary

def main():
    text = get_book_text("books/frankenstein.txt")
    #print(text)
    count = get_word_count("books/frankenstein.txt")
    #print(f"{count} words found in the document")
    dictionary = get_book_dictionary(text)
    print(dictionary)

    

main()
