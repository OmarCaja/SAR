#!/usr/bin/python

import sys

def crear_indice(frases):
    index = {}
    for frase in frases:
        for word1, word2 in zip(frase.split()[:-1], frase.split()[1:]):
            if (index.get(word1)):
                index[word1][0] += 1
                index[word1][1][word2] = index[word1][1].get(word2, 0) + 1
            else:
                index[word1] = [1, {word2 : 1}]
    return index
        

def obtener_frases(texto):
    return 1

def formatear_indice(index):
    return 1

def guardar_indice(filename):
    return None

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
        guardar_indice(sys.argv[2])