"""Word Finder: finds random words from a dictionary."""

import random

# https://stackoverflow.com/questions/18834636/random-word-generator-python
class WordFinder:
    '''Get list of words from online dictionary and return random word'''
    def __init__(self,file):
        words = []
        text_file=open(file)
        for word in text_file:
            words.append(word)
        self.words=words
        
    def random(self):
        word = random.choice(self.words)
        return word.strip('\n')

class SpecialWordFinder:
    '''Return list of words that has # and blank spaces removed'''
    def cleaned_list(self,file):
        return[word.strip() for word in file
            if word.strip() and not word.starswith("#")]
