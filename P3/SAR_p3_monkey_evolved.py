#!/usr/bin/python

import sys
import pickle

def syntax_error():
    print("you must provide an index file")

def load_index(filename):
    with open(filename, "rb") as fh:
        index = pickle.load(fh)
    return index

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        syntax_error()
    else:
        index = load_index(sys.argv[1])