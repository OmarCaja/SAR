#!/usr/bin/python3

"""
1.- Pig Latin versión ampliada

Nombre Alumno: Omar Caja García
"""

import sys

args = sys.argv

punctuation_marks = [',', ';', '.', '?', '!']

lower_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
upper_vowels = ['A', 'E', 'I', 'O', 'U', 'Y']

lower_vowels_ending = ['y', 'a', 'y']
upper_vowels_ending = ['Y', 'A', 'Y']

lower_consonants_ending = ['a', 'y']
upper_consonants_ending = ['A', 'Y']

def string_to_list(word):
    return list(word)

def list_to_string(list):
    return ''.join(list)

def star_with_vowel(word):
    return word in lower_vowels or word in upper_vowels

def index_first_vocal(list):
    count = 0

    for char in list:
        if char not in lower_vowels and char not in upper_vowels:
            count += 1
        else:
            break

    return count

def check_punctuation_mark(list):
    return list[-1] in punctuation_marks

def count_upper_cases(list):
    count = 0

    for char in list:
        if char.isupper():
            count += 1
    
    return count

def to_upper_case(list):
    return [x.upper() for x in list]

def piglatin_word(word):
    word_list = string_to_list(word)
    first_char = word_list[0]
    punctuation_mark = []

    num_uppers = count_upper_cases(word_list)

    if check_punctuation_mark(word_list):
        punctuation_mark = [word_list[-1]]
        word_list.pop()

    if first_char.isalpha():

        if star_with_vowel(first_char):

            if num_uppers == len(word):
                word_list = to_upper_case(word_list) + upper_vowels_ending    
            
            else:
                word_list = word_list + lower_vowels_ending

        else:
            first_vocal = index_first_vocal(word_list)

            if num_uppers == 1:
                word_list[0] = word_list[0].lower()
                word_list[first_vocal] = word_list[first_vocal].upper()
                word_list = word_list[first_vocal:] + word_list[:first_vocal] + lower_consonants_ending
            
            elif num_uppers == len(word):
                word_list = to_upper_case(word_list)
                word_list = word_list[first_vocal:] + word_list[:first_vocal] + upper_consonants_ending

            else:
                word_list = word_list[first_vocal:] + word_list[:first_vocal] + lower_consonants_ending

    return list_to_string(word_list + punctuation_mark)

def piglatin_sentence(sentence):
    words_list = sentence.split()
    word_list_result = []

    for word in words_list:
        word_list_result.append(piglatin_word(word))

    return " ".join(word_list_result)

if len(args) == 1:
    finish = False

    print("---------- Pulse enter para finalizar el programa ---------- \n")

    while not finish:
        sentence = input("Introduzca una frase \n\n")
        finish = not sentence

        translated_sentence = piglatin_sentence(sentence) 

        print("\n" + translated_sentence + "\n")

elif len(args) == 2:
    sentence = args[1]
    print("Hay una frase en la línea de comandos " + sentence + "\n")
    print(piglatin_sentence(sentence))

elif len(args) == 3:
    read_file = open(args[2])
    write_file = open(args[2][:4] + "_piglatin.txt","w+")

    line = read_file.readline()

    while line:
        write_file.write(piglatin_sentence(line) + "\n")
        line = read_file.readline()

    read_file.close()
    write_file.close()

sys.exit("---------- Programa finalizado ----------")