import re


def get_words(sentence):
    sentence = re.sub('[!@#$%^&*()_+/\\\,.?:;\'"]', '', sentence)
    sentence = sentence.lower()
    sentence = sentence.strip()
    sentence = sentence.split()

    return set(sentence)


def get_item(sentence):
    sentence = re.sub('[(),\']', '', str(sentence))
    return sentence

