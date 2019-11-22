import string
def cleanWord(w):
    return w.lower().strip(string.punctuation)

def splitWords(phrase):
    phrase = cleanWord(phrase)
    words = phrase.split()
    words_set = set()
    for word in words:
        words_set.add(word)
    return words_set