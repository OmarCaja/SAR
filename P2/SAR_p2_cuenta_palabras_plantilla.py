#! /usr/bin/python
#! -*- encoding: utf8 -*-

from operator import itemgetter
import re
import sys

stopwords = []
dict_words = {}
dict_symbols = {}

line_counter = 0
word_counter = 0
symbol_counter = 0

clean_re = re.compile('\W+')

def clean_text(text):
    return clean_re.sub(' ', text)

def sort_dic(d):
    for key, value in sorted(d.items(), key=itemgetter(1), reverse=True):
        yield key, value

def text_statistics(filename, to_lower=True, remove_stopwords=True):
    global line_counter
    file_doc = open(name, 'r')
    for sentence in file_doc.readlines():
        line_counter = line_counter + 1
        sentence = clean_text(sentence)
        count_words(sentence)
    return stats()

def count_words(sentence):
    global word_counter
    for word in sentence.split():
        word_counter += 1
        if word.lower() not in stopwords:
            dict_words[word] = dict_words.get(word, 0) + 1
            count_symbols(word)

def count_symbols(word):
    global symbol_counter
    for symbol in word:
        symbol_counter += 1
        dict_symbols[symbol] = dict_symbols.get(symbol, 0) + 1
            
def stats():
    print(line_counter)
    print(word_counter)
    print(symbol_counter)

def syntax():
    print ("\n%s filename.txt [to_lower?[remove_stopwords?]\n" % sys.argv[0])
    sys.exit()

if __name__ == "__main__":
    file_stop = open('stopwords_en.txt', 'r')
    for word in file_stop.readlines():
        stopwords.append(word[:-1])

    if len(sys.argv) < 2:
        syntax()
    name = sys.argv[1]

    lower = False
    stop = False
    if len(sys.argv) > 2:
        lower = (sys.argv[2] in ('1', 'True', 'yes'))
        if len(sys.argv) > 3:
            stop = (sys.argv[3] in ('1', 'True', 'yes'))
    text_statistics(name, to_lower=lower, remove_stopwords=stop)
