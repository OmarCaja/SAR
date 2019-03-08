#!/usr/bin/env python

import os
from whoosh.index import create_in
from whoosh.fields import Schema, ID, TEXT
import argparse

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

    writer = ix.writer()
    writer.add_document(title="First document", path="/a",
                    content="Este es el texto del primer documento_")
    writer.add_document(title="Second document", path="/b",
                    content="Este es el TEXTO de nuestro segundo documento")
    writer.commit()



