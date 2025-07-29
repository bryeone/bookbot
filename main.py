from stats import get_word_count
from stats import get_book_text
from stats import get_book_dictionary
from stats import sort_dict
from stats import sort_on

def main():
    text = get_book_text("books/frankenstein.txt")
    #print(text)
    count = get_word_count("books/frankenstein.txt")
    #print(f"{count} words found in the document")
    dictionary = get_book_dictionary(text)
    sorted_dictionary = sort_dict(dictionary)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for i in sorted_dictionary:
        print(f"{i["char"]}: {i["num"]}")
        #print(sorted_dictionary)

    

main()
