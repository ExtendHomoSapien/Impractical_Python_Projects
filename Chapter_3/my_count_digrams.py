"""Write a python program that finds all the digrams in 'tmvoordle' and then counts their frequency of occurrence in
a dictionary file. Be sure to test your code on words like volvo, so you don't overlook repeating digrams in the same
word. """

import word_dictionary_util.load_dictionary as load_dictionary
from collections import Counter


# load dictionary
# split word into bigrams
# loop dictionary and find bigrams, if match, add to count

def make_bigrams(word: str) -> list:
    """split word into bigrams"""
    out_bigrams = list()
    for i in range(0, len(word) - 1):
        bigram = word[i] + word[i + 1]
        out_bigrams.append(bigram)
    return out_bigrams

def filter_bigrams(word: str, target_bigrams: list) -> list:
    """return list of bigrams matching target bigrams"""
    pass

def main():
    dict_file = load_dictionary.load()
    input_word = 'tmvoordle'
    bigram_dict = Counter(make_bigrams(input_word))
    filtered_bigrams = []

    # for bigram in make_bigrams(input_word):
    #     print(f"finding bigram counts for '{bigram}'")
    #     for word in dict_file:
    #         word


if __name__ == "__main__":
    main()
