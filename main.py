from stats import word_count, char_count
import sys

def get_book_text(book_file):
    contents = book_file.read()
    return contents 

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
        print(f"Reading from: {book_path}")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  
    with open(book_path) as book_file:
        book_contents = get_book_text(book_file)
        
    print(book_contents)

    word_count_result = word_count(book_contents)
    print(f"Found {word_count_result} total words")

    char_count(book_contents)
 
main()