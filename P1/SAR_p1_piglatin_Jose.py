#!/usr/bin/env python
#! -*- encoding: utf8 -*-

"""
1.- Pig Latin

Nombre Alumno: Jose Antonio Culla de Moya

Nombre Alumno:

Se ha implementado la ampliacion
"""

import sys
import re
import argparse



def piglatin_word(word):
    """
    Esta función recibe una palabra en inglés y la traduce a Pig Latin

    :param word: la palabra que se debe pasar a Pig Latin
    :return: la palabra traducida
    """
    vocales = "aeiouy"
    word2 = word
    if word[0].isalpha():
    	if (word[0].lower() in vocales):
   			word2 = word + 'yay'
    	else:
    		index = 0
    		for char in word.lower():
    			if char in vocales:
    				index = word.lower().index(char)
    				break
    		word2 = (word[index:] + word[0:index] + 'ay').lower()
    		if word[0].isupper():
    			word2 = word2.capitalize()
    		if word.isupper():
    			word2 = word2.upper()
    return word2


def piglatin_sentence(sentence):
    """
    Esta función recibe una frase en inglés i la traduce a Pig Latin

    :param sentence: la frase que se debe pasar a Pig Latin
    :return: la frase traducida
    """
    er = re.compile("(\w+)(\W*)")
    new_sentence = ''
    for word, puntuation in er.findall(sentence):
    	new_sentence += piglatin_word(word) + puntuation
    return  new_sentence


if __name__ == "__main__":

    """
    Se realiza el tratamiento de los agrumentos introducidos en la llamada
    al programa y se actua en consecuencia
    
    Incluye la funcionalidad para leer desde fichero
    """

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("frase", nargs="*", help="frase que se desea traducir")
    parser.add_argument("-f", help="F es el nombre de un fichero a traducir")
    
    args = parser.parse_args()
    filename = args.f
    frase = ' '.join(args.frase)

    if frase:
        print(piglatin_sentence(frase))
    else:
        if filename:
            if filename[-4:] == ".txt":
                fichero = open(filename, "r")
                ficheroGuardado = open(filename[:-4] + "_piglatin.txt", "w")
                for sentence in fichero.readlines():
                    ficheroGuardado.write(piglatin_sentence(sentence))
                ficheroGuardado.flush()
                ficheroGuardado.close()
                fichero.close()
        else:       
            while True:
                sentence = raw_input("ENGLISH: ")
                if len(sentence) == 0:
                    break
                print("PIG LATIN: " + piglatin_sentence(sentence))