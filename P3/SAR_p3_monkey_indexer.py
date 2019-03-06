#!/usr/bin/python

import sys
import re
import pickle

def crear_indice(frases):
    index = {}
    for frase in frases:
        frase = "$ " + clean_text(frase) + " $"
        for word1, word2 in zip(frase.split()[:-1], frase.split()[1:]):
            if (index.get(word1)):
                index[word1][0] += 1
                index[word1][1][word2] = index[word1][1].get(word2, 0) + 1
            else:
                index[word1] = [1, {word2 : 1}]
    return index
        
clean_re = re.compile('\W+')

def clean_text(text):
    return clean_re.sub(' ', text)

def obtener_frases(texto):
    return texto.replace(";", "\n\n").replace("!", "\n\n") \
        .replace(".", "\n\n").replace("?","\n\n") \
        .lower().split("\n\n")

def formatear_indice(index):
    for key, value in index.items():
        word_list = []
        for key2, value2 in value[1].items():
            word_list.append((value2, key2))
        index[key] = (value[0], word_list)
    return index

def guardar_indice(indice, filename):
    with open(filename, "wb") as fh:
        pickle.dump(indice, fh)

def syntax_error():
    print("debe introducir como argumento el nombre de dos ficheros")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        syntax_error()
    else:
        input = open(sys.argv[1], "r")
        texto = "".join(input.readlines())
        input.close()
        frases = obtener_frases(texto)
        index = crear_indice(frases)
        index = formatear_indice(index)
        print(index)
        guardar_indice(index, sys.argv[2])