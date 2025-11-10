def get_word_count(text):
    """
    Counts the number of words in a string
    Args:
        text (str): The text to count words from
    Returns:
        int: The number of words in the text
    """
    words = text.split()
    return len(words)

def get_char_count(text):
    """
    Counts occurrences of each character in a string
    Args:
        text (str): The text to count characters from
    Returns:
        dict: Dictionary with characters as keys and their counts as values
    """
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_count(char_count):
    """
    Converts character count dictionary to sorted list of dictionaries
    Args:
        char_count (dict): Dictionary of character counts
    Returns:
        list: Sorted list of dictionaries with char and count information
    """
    sorted_list = []
    for char, count in char_count.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list


