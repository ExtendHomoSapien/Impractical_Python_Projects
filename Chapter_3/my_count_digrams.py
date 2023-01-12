"""Write a python program that finds all the digrams in 'tmvoordle' and then counts their frequency of occurrence in
a dictionary file. Be sure to test your code on words like volvo, so you do't overlook repeating digrams in the same
word. """


# load dictionary
# split word into bigrams
# loop dictionary and find bigrams, if match, add to count

def make_bigrams(word: str) -> set:
    """split word into digrams"""
    out_bigrams = set()
    for i in range(0, len(word) - 1):
        bigram = word[i] + word[i + 1]
        out_bigrams.add(bigram)
    return out_bigrams
