def get_word_count(file_path):
    text = get_book_text(file_path)
    word_count = len(text.split())
    return word_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def get_book_dictionary(text):
    text = text.lower()
    word_text = text.split()
    dictionary = {}

    for word in word_text:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] = dictionary[word] + 1
    return dictionary
    
            

