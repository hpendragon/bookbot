import sys
from stats import get_word_count, get_char_count, sort_char_count

def get_book_text(filepath):
    """
    Reads and returns the contents of a text file as a string
    Args:
        filepath (str): Path to the text file
    Returns:
        str: Contents of the text file
    """
    with open(filepath, 'r') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    
    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: Could not find file at {book_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Could not read file at {book_path}")
        print(e)
        sys.exit(1)
        
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    sorted_chars = sort_char_count(char_count)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"Found {word_count} total words")
    print("\n--- Character Counts ---")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("--- End report ---")

if __name__ == "__main__":
    main()
