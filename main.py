from stats import get_word_count, create_symbol_dict, creating_dict_list
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    standard_path = "/Users/karl/coding/boot.dev/bookbot/"
    if sys.argv:
        if len(sys.argv) < 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        else:
            book_path = str(sys.argv[1])
    book = get_book_text(standard_path + book_path)
    num_words = get_word_count(book)
    letters_dict = create_symbol_dict(book)
    sorted_dict_list = creating_dict_list(letters_dict)

    
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------")
    print(f"Found {num_words} total words\n--------- Character Count -------")
    for entry in sorted_dict_list:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")
    
    
if __name__ == "__main__":
    main()
