from collections import Counter

def word_count(book_contents):
    words = book_contents.split()
    return len(words)

def char_count(book_contents):
    book_contents = book_contents.lower()
    character_counts = {}
    for character in book_contents:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
            
    for character, count in character_counts.items():
        print(f"'{character}': {count}")