from stats import *
import sys

def main():
    # Previous code that was refactored for final submission
    #print("greetings boots")
    #print(get_book_text("books/frankenstein.txt"))
    #print(f"{get_num_words(get_book_text('books/frankenstein.txt'))} words found in the document")
    #print(get_num_chars(get_book_text('books/frankenstein.txt')))
    #filepath = "books/frankenstein.txt"
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    sorted_chars = get_sorted_chars(num_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count -----------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["count"]}")
    print("============= END ===============")

if __name__ == "__main__":

    main()