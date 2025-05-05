from collections import Counter

def word_count(book_contents):
    words = book_contents.split()
    return len(words)

def char_count(book_contents):
    book_contents = book_contents.lower()
    character_counts = {}
    for character in book_contents:
        if not character.isalpha():
            continue
        if character in character_counts:
                character_counts[character] += 1
        else:
                character_counts[character] = 1

    sorted_counts = sorted(character_counts.items(), key=lambda item: item[1], reverse=True)

    for character, count in sorted_counts:
        print(f"{character}: {count}")

