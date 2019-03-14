#!/usr/bin/env python

'''
Jose Antonio Culla de Moya
Omar Caja Garcia
'''

import os
from whoosh.index import create_in
from whoosh.fields import Schema, ID, TEXT, KEYWORD, DATETIME, STORED
import argparse
import json

def add_to_index(filename, index):
    file = get_file_info(filename)
    writer = index.writer()
    writer.add_document(id=file["id"], title=file["title"], article=file["article"],
        keywords=file["keywords"], date=file["date"], path=filename)
    writer.commit()

def get_file(docs_dir):
    for dirname, _, files in os.walk(docs_dir):
        for filename in files:
            yield os.path.join(dirname, filename)

def get_file_info(filename):
    with open(filename, "r") as fh:
        return json.load(fh)

def create_index(index_dir):
    schema = Schema(id=ID, title=TEXT(stored=True), article=TEXT, keywords=KEYWORD(stored=True),
        path=STORED, date=DATETIME(stored=True))
    
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
        add_to_index(filename, index)