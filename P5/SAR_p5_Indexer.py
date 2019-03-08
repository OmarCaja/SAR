#!/usr/bin/env python

import os
from whoosh.index import create_in
from whoosh.fields import Schema, ID, TEXT
import argparse

def add_to_index(file, index):
    writer = index.writer()
    '''index.add_document(title)'''
    writer.commit()

def get_file(docs_dir):
    for dirname, _, files in os.walk(docs_dir):
        for filename in files:
            yield os.path.join(dirname, filename)

def get_file_info(filename):
    with open(filename, "r") as fh:
        return json.load(fh)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("doc_directory", help="directory where docs for teh index are")
    parser.add_argument("index_directory", help="directory where the index will be saved")

    args = parser.parse_args()

    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
    idir = args.index_directory

    if not os.path.exists(idir):
        os.mkdir(idir)

    ix = create_in(idir, schema)

    for filename in get_file(args.doc_directory):
        add_to_index(get_file_info(filename), ix)