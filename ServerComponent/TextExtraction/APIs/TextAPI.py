from spellchecker import SpellChecker
import string
from langdetect import detect
from autocorrect import Speller
from nltk import sent_tokenize


def getWordsNumber(text):
    if text == "ERROR404:Data not found":
        return 0
    return len(text.split())


# Version 1(more safe)
def getWrongWordsNumber(text):
    if text == "ERROR404:Data not found":
        return 0
    spell = SpellChecker()

    text = text.replace('\'s', ' ')
    text = text.translate(str.maketrans('', '', string.punctuation))
    misspelled = text.split()
    lis = []
    for word in misspelled:
        if word != word.capitalize():
            correction = spell.correction(word)
            if word != correction:
                lis.append(correction)
                print(word, spell.correction(word))
                # print(spell.candidates(word))

    return len(lis)


def detectLanguage(text):
    return detect(text)


# Version 2(faster)
def getWrongWordsNumbers(text):
    if text == "ERROR404:Data not found":
        return 0
    spell = Speller(lang='en')

    text = text.replace('\'s', ' ')
    text = text.translate(str.maketrans('', '', string.punctuation))
    misspelled = text.split()
    lis = []
    for word in misspelled:
        if word != word.capitalize():
            possibleWord = spell(word)
            if word != possibleWord:
                lis.append(word)
                # print(word, possibleWord)

    return len(lis)


def calculateNumber(number):
    if '.' in number:
        number = number.replace('.', '')
        if 'K' in number:
            number = number.replace('K', '00')
    else:
        if 'K' in number:
            number = number.replace('K', '000')
    return int(number)

def getListOfSentences(text):
    return sent_tokenize(text)

# TODO: https://github.com/emilmont/pyStatParser
