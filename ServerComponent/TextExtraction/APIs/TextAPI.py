from spellchecker import SpellChecker
import string
from langdetect import detect
from autocorrect import Speller


def getWordsNumber(text):
    return len(text.split())

#Version 1(more safe)
def getWrongWordsNumber(text):
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

#Version 2(faster)
def getWrongWordsNumbers(text):
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
                #print(word, possibleWord)

    return len(lis)


#TODO: https://github.com/emilmont/pyStatParser