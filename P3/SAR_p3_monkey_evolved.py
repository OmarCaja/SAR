#!/usr/bin/python

'''
Jose Antonio Culla de Moya
Omar Caja García

Implementada la ampliacion, no es necesario ningun comando especial

'''

import sys
import pickle
import random

def syntax_error():
    print("you must provide an index file")

def load_index(filename):
    with open(filename, "rb") as fh:
        index = pickle.load(fh)
    return index

def generate_sentence(index):
    word = next_word(index["$"][1])
    sentence = "$ " + word
    while (word != "$" and len(sentence.split()) < 25):
        word = next_word(index[word][1])
        sentence = sentence + " " + word
    return sentence

def generate_sentence_tri(index):
    word = next_word(index[tuple(["$", "$"])][1])
    sentence = "$ " + word
    while (word != "$" and len(sentence.split()) < 25):
        words_list = sentence.split()
        words = [words_list[words_list.index(word)- 1], words_list[words_list.index(word)]]
        word = next_word(index[tuple(words)][1])
        sentence = sentence + " " + word
    return sentence
        
def next_word(word_occurence_list):
    choice_list = generate_choice_list(word_occurence_list)
    return random.choice(choice_list)[0]

def generate_choice_list(word_occurence_list):
    choice_list = []
    for number, word in word_occurence_list:
        choice_list.append(((word + " ") * number).split())
    return choice_list


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        syntax_error()
    else:
        index = load_index(sys.argv[1])
        keys = index.keys()
        for i in range(0, 10):
            if(isinstance(keys[0], str)):
                print(generate_sentence(index))
            else:
                print(generate_sentence_tri(index))