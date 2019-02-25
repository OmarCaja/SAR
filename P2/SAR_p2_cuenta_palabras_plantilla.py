#! /usr/bin/python

from operator import itemgetter
import re
import sys

stopwords = []
dict_words = {}
dict_symbols = {}

line_counter = 0
word_counter = 0
stopwords_counter = 0
symbol_counter = 0

clean_re = re.compile('\W+')

def clean_text(text):
    return clean_re.sub(' ', text)

def sort_dic(d):
    for key, value in sorted(d.items(), key=itemgetter(1), reverse=True):
        yield key, value

def print_dic_alphabetically(d):
    alphabetical_keys = sorted(d.keys())
    for key in alphabetical_keys:
        print('\t' + str(key) + '\t' + str(d[key]))

def print_dic_by_frecuency(d):
    for item in sort_dic(d):
        print('\t' + str(item[0]) + '\t' + str(item[1]))

def to_lower_case(sentence):
    return sentence.lower()

def text_statistics(filename, to_lower, remove_stopwords):
    global line_counter
    file_doc = open(filename, 'r')

    for sentence in file_doc.readlines():
        line_counter = line_counter + 1
        sentence = clean_text(sentence)

        if to_lower:
           sentence = to_lower_case(sentence)

        count_words(sentence, remove_stopwords)
        
    return stats(remove_stopwords)

def count_words(sentence, remove_stopwords):
    global word_counter
    global stopwords_counter

    for word in sentence.split():
        word_counter += 1

        if remove_stopwords and word in stopwords:
            stopwords_counter += 1
            continue

        count_symbols(word)
        dict_words[word] = dict_words.get(word, 0) + 1

def count_symbols(word):
    global symbol_counter

    for symbol in word:
        symbol_counter += 1
        dict_symbols[symbol] = dict_symbols.get(symbol, 0) + 1
            
def stats(remove_stopwords):
    print('Lines: ' + str(line_counter))
    print('Number of words (with stopwords): ' + str(word_counter))

    if remove_stopwords:
        print('Number of words (without stopwords): ' + str(word_counter - stopwords_counter))

    print('Vocabulary size: ' + str(len(dict_words)))
    print('Number of symbols: ' + str(symbol_counter))
    print('Number of different symbols: ' + str(len(dict_symbols)))

    print('Words (alphabetical order):')
    print_dic_alphabetically(dict_words)

    print('Words (by frequency):')
    print_dic_by_frecuency(dict_words)

    print('Symbols (alphabetical order):')
    print_dic_alphabetically(dict_symbols)

    print('Symbols (by frequency):')
    print_dic_by_frecuency(dict_symbols)

def syntax():
    print ("\n%s filename.txt [to_lower?][remove_stopwords?]\n" % sys.argv[0])
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