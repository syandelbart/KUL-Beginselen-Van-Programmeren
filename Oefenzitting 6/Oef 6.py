key = {"a":"n", "b":"o", "c":"p", "d":"q", "e":"r", "f":"s", "g":"t",
"h":"u", "i":"v", "j":"w", "k":"x", "l":"y", "m":"z", "n":"a", "o":"b",
"p":"c", "q":"d", "r":"e", "s":"f", "t":"g", "u":"h", "v":"i", "w":"j",
"x":"k", "y":"l", "z":"m", "A":"N", "B":"O", "C":"P", "D":"Q", "E":"R",
"F":"S", "G":"T", "H":"U", "I":"V", "J":"W", "K":"X", "L":"Y", "M":"Z",
"N":"A", "O":"B", "P":"C", "Q":"D", "R":"E", "S":"F", "T":"G", "U":"H",
"V":"I", "W":"J", "X":"K", "Y":"L", "Z":"M"}

import string
def splitWords(phrase):
    phrase.strip(string.punctuation)
    words = phrase.split()
    return words

def splitByChar(word):
    return [char for char in word]

strng = ""
message = str(input("Input your message:"))
message_array = splitWords(message)
keys = list(key.keys())
values = list(key.values())
for message_word in message_array:
    word_array = splitByChar(message_word)
    for char in word_array:
        if string.punctuation.count(char) > 0:
            strng += char
        else:
            strng += key[char]
    strng += " "

dec_str = ""
for message_word in message_array:
    word_array = splitByChar(message_word)
    for char in word_array:
        if string.punctuation.count(char) > 0:
            dec_str += char
        else:
            dec_str += keys[values.index(char)]
    dec_str += " "



print("Decoder:",strng)
print("Encoder:",dec_str)