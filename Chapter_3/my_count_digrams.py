"""
Capture digram stats on a dictionary.

Write a python program that finds all the digrams in 'tmvoordle' and then counts their frequency of occurrence in
a dictionary file. Be sure to test your code on words like volvo, so you don't overlook repeating digrams in the same
word.
"""

import word_dictionary_util.load_dictionary as load_dictionary
from collections import Counter


# load dictionary
# split word into digrams
# loop dictionary and find digrams, if match, add to count

def make_digrams(word: str) -> list:
    """Split word into digrams."""
    out_digrams = list()
    for i in range(0, len(word) - 1):
        bigram = word[i] + word[i + 1]
        out_digrams.append(bigram)
    return out_digrams


def intersection(candidate: list, control: list):
    """Filter candidate list by control list."""
    temp = set(control)
    filtered = [value for value in candidate if value in temp]
    return filtered


def filter_digrams(word: str, target_digrams: list) -> list:
    """Return list of digrams matching target digrams."""
    return intersection(candidate=make_digrams(word), control=target_digrams)


def main():
    """Control logic."""
    dict_file = load_dictionary.load()
    input_word = 'tmvoordle'
    input_digrams = set(make_digrams(input_word))
    filtered_digrams = []
    for word in dict_file:
        filtered_digrams.extend(
            filter_digrams(word=word, target_digrams=list(input_digrams))
        )
    bg_cntr = Counter(filtered_digrams)
    print(bg_cntr.most_common())


if __name__ == "__main__":
    main()
