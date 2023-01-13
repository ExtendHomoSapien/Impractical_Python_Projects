"""
Capture bigram stats on a dictionary.

Write a python program that finds all the bigrams in 'tmvoordle' and then counts their frequency of occurrence in
a dictionary file. Be sure to test your code on words like volvo, so you don't overlook repeating bigrams in the same
word.
"""

import word_dictionary_util.load_dictionary as load_dictionary
from collections import Counter


# load dictionary
# split word into bigrams
# loop dictionary and find bigrams, if match, add to count

def make_bigrams(word: str) -> list:
    """Split word into bigrams."""
    out_bigrams = list()
    for i in range(0, len(word) - 1):
        bigram = word[i] + word[i + 1]
        out_bigrams.append(bigram)
    return out_bigrams


def intersection(candidate: list, control: list):
    """Filter candidate list by control list."""
    temp = set(control)
    filtered = [value for value in candidate if value in temp]
    return filtered


def filter_bigrams(word: str, target_bigrams: list) -> list:
    """Return list of bigrams matching target bigrams."""
    return intersection(candidate=make_bigrams(word), control=target_bigrams)


def main():
    """Control logic."""
    dict_file = load_dictionary.load()
    input_word = 'tmvoordle'
    input_bigrams = set(make_bigrams(input_word))
    filtered_bigrams = []
    for word in dict_file:
        filtered_bigrams.extend(
            filter_bigrams(word=word, target_bigrams=list(input_bigrams))
        )
    bg_cntr = Counter(filtered_bigrams)
    print(bg_cntr.most_common())


if __name__ == "__main__":
    main()
