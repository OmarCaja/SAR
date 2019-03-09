#!/usr/bin/env python

from whoosh.index import open_dir
from whoosh.qparser import QueryParser
import argparse

def syntax():
    return "python SAR_p5_Searcher.py index_directory [-q=query] [--extend]"

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(usage=syntax())
    parser.add_argument("index", help="index file")
    parser.add_argument("-q", help="query to search")
    parser.add_argument("--extend", action="store_true", help="indicates if you want all the information")

    args = parser.parse_args()

    ix = open_dir(args.index)
    with ix.searcher() as searcher:
        if args.q:
            hola = 1
        else:
            while True:
                text = input("Dime:")
                if len(text) == 0:
                    break
                query = QueryParser("content", ix.schema).parse(text)
                results = searcher.search(query)
                for r in results:
                    print(r)

