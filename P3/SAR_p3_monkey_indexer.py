#!/usr/bin/python

import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        syntax_error()
    else:
        input = open(sys.argv[1], "r")
        texto = "".join(input.readlines())
        frases = obtener_frases()
        crear_indice(frases)

def crear_indice(frases):
    for frase in frases:
        

def obtener_frases(texto):


def syntax_error():
    print("debe introducir como argumento el nombre de dos ficheros")