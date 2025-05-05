from stats import word_count, char_count

def get_book_text(book_file):
    contents = book_file.read()
    return contents 

def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as book_file:
        book_contents = get_book_text(book_file)
        
    print(book_contents)

    word_count_result = word_count(book_contents)
    print(f"{word_count_result} words found in the document")

    char_count(book_contents)
 
main()