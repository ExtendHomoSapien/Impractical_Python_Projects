"""So here's how we can recursively determine whether a string is a palindrome. If the first and last letters differ,
then declare that the string is not a palindrome. Otherwise, strip off the first and last letters, and determine
whether the string that remains—the subproblem—is a palindrome. Declare the answer for the shorter string to be the
answer for the original string. Once you get down to a string with no letters or just one letter, declare it to be a
palindrome. """


def is_palindrome(word: str) -> bool:
    if word == '' or len(word) == 1:
        return True
    if word[0:1] == word[-1:]:
        less_word = word.lstrip(word[0:1]).rstrip(word[0:1])
        return is_palindrome(less_word)

    return False


if __name__ == "__main__":
    eval_words = [
        'ewe',
        'ewok', 'broken', 'typical', 'evaporate', 'racecar'
    ]
    p_count = 0
    for w in eval_words:
        print(f'Evaluating "{w}" for palindrome')
        if is_palindrome(w):
            print(f'"{w}" is palindrome')
            p_count += 1

    print(f'Total palindromes in list: {p_count}')
    print(f'Total words in list: {len(eval_words)}')
