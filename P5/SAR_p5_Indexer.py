#!/usr/bin/env python

import os
from whoosh.index import create_in
from whoosh.fields import Schema, ID, TEXT
import argparse
import json

def add_to_index(file, index):
    writer = index.writer()
    writer.add_document(title=file["title"], path=file["url"], content=file["article"])
    writer.commit()

def get_file(docs_dir):
    for dirname, _, files in os.walk(docs_dir):
        for filename in files:
            yield os.path.join(dirname, filename)

def get_file_info(filename):
    with open(filename, "r") as fh:
        return json.load(fh)

def create_index(index_dir):
    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
    
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)

    return create_in(index_dir, schema)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("doc_directory", help="directory where docs for teh index are")
    parser.add_argument("index_directory", help="directory where the index will be saved")

    args = parser.parse_args()

    index = create_index(args.index_directory)

    for filename in get_file(args.doc_directory):
        add_to_index(get_file_info(filename), index)