import string
def cleanWord(w):
    return w.lower().strip(string.punctuation)

def splitWords(phrase):
    phrase = cleanWord(phrase)
    words = phrase.split()
    return words


user_input = str(input("Input a text: "))
list_for_all_words = list()

word_collection = list()
occurance_collection = list()

total_length = 0
while user_input != "QQQ":
    words_list = splitWords(user_input)
    list_for_all_words.append(words_list)

    added_words = []
    for word in words_list:
        if word_collection.count(word) == 0:
            added_words.append(word)
            word_collection.append(word)
            occurance_collection.append(1)
        else:
            occurance_collection[word_collection.index(word)] += 1

    print("New size of the vocabulary:",len(word_collection))
    print("Words newly added:",added_words)
    user_input = str(input("Input a text: "))

word_cursor = 0
for word in word_collection:
    print(word,occurance_collection[word_cursor])
    word_cursor += 1