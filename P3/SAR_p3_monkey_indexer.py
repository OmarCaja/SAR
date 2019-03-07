#!/usr/bin/python

import sys
import re
import pickle
import argparse

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

def create_trigram_index(frases):
    index = {}
    for frase in frases:
        frase = "$ $ " + clean_text(frase) + " $"
        for word1, word2, word3 in zip(frase.split()[:-1], frase.split()[1:], frase.split()[2:]):
            if (index.get(tuple([word1, word2]))):
                index[tuple(tuple([word1, word2]))][0] += 1
                index[tuple([word1, word2])][1][word3] = index[tuple([word1, word2])][1].get(word3, 0) + 1
            else:
                index[tuple([word1, word2])] = [1, {word3 : 1}]
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
        for key2, value2 in sort_dic(value[1]):
            word_list.append((value2, key2))
        index[key] = (value[0], word_list)
    return index

def sort_dic(d):
    for key, value in sorted(d.items(), key=lambda a: (-a[1], a[0])):
        yield key, value

def guardar_indice(indice, filename):
    with open(filename, "wb") as fh:
        pickle.dump(indice, fh)

def syntax_error():
    print("debe introducir como argumento el nombre de dos ficheros")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("text_filename", help="fichero de texto de entrada")
    parser.add_argument("index_filename", help="fichero de salida")
    parser.add_argument("-tri", action="store_true",help="argumento que indica si se desea el indice con trigramas")
    
    args = parser.parse_args()
    input_filename = args.text_filename
    output_filename = args.index_filename

    input = open(input_filename, "r")
    texto = "".join(input.readlines())
    input.close()
    frases = obtener_frases(texto)

    if args.tri:
        index = create_trigram_index(frases)
    else:
        index = crear_indice(frases)

    index = formatear_indice(index)
    print(index)
    guardar_indice(index, output_filename)