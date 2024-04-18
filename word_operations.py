def words_longer_than_n_no_builtin(string, n):
    """
    Returns a list of words longer than n characters from a given string without using built-in Python functions.
    
    Args:
    string (str): The input string.
    n (int): The minimum length of words to consider.
    
    Returns:
    list: A list of words longer than n characters.
    """
    words = []
    current_word = ''
    for char in string:
        if char != ' ':
            current_word += char
        else:
            words.append(current_word)
            current_word = ''
    words.append(current_word)  # Add the last word
    out_list = []
    for word in words:
        if len(word)>n:
            out_list.append(word)
    return out_list

def is_palindrome_no_builtin(word):
    """
    Checks if a word is a palindrome without using built-in Python functions.
    
    Args:
    word (str): The input word to check.
    
    Returns:
    bool: True if the word is a palindrome, False otherwise.
    """
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return True


def words_longer_than_n(string, n):
    """
    Returns a list of words longer than n characters from a given string.
    
    Args:
    string (str): The input string.
    n (int): The minimum length of words to consider.
    
    Returns:
    list: A list of words longer than n characters.
    """
    words = string.split()
    longer_words = [word for word in words if len(word) > n]
    return longer_words

def is_palindrome(word):
    """
    Checks if a word is a palindrome.
    
    Args:
    word (str): The input word to check.
    
    Returns:
    bool: True if the word is a palindrome, False otherwise.
    """
    return word == word[::-1]



if __name__ == "__main__":
    # Example usage of words_longer_than_n function
    string = 'The quick brown fox jumps over the lazy dog'
    n = 4
    longer_words = words_longer_than_n(string, n)
    print(f"Words longer than {n} characters: {longer_words}")

    # Example usage of words_longer_than_n_no_builtin function
    string = 'The quick brown fox jumps over the lazy dog'
    n = 4
    longer_words_no_builtin = words_longer_than_n_no_builtin(string, n)
    print(f"Words longer than {n} characters without using built-in functions: {longer_words_no_builtin}")
    
    # Example usage of is_palindrome function
    words_list = ['sheep', 'xenex', 'cow', 'radar', 'level']
    for word in words_list:
        print(f"{word} is a palindrome: {is_palindrome(word)}")

    # Example usage of is_palindrome_no_builtin function
    words_list = ['sheep', 'xenex', 'cow', 'radar', 'level']
    for word in words_list:
        print(f"{word} is a palindrome without using built-in functions: {is_palindrome_no_builtin(word)}")
