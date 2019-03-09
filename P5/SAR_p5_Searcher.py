#!/usr/bin/env python

from whoosh.index import open_dir
from whoosh.qparser import QueryParser
import argparse

def syntax():
    return "python SAR_p5_Searcher.py index_directory [-q=query] [--extend]"

def search(text, index):
    with index.searcher() as searcher:
        query = QueryParser("article", index.schema).parse(text)
        return searcher.search(query)

def print_default(results):
    for result in results:
        print(result)

def print_extended(results):
    for result in results:
        print(result)

def print_results(results, extended):
    if extended:
        print_extended(results)
    else:
        print_default(results)
    print("=================")
    print(len(results) + "results")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(usage=syntax())
    parser.add_argument("index", help="index directory")
    parser.add_argument("-q", help="query to search")
    parser.add_argument("--extend", action="store_true", help="indicates if you want all the information")

    args = parser.parse_args()

    index = open_dir(args.index)
    
    if args.q:
        results = search(args.q, index)
        print_results(results, args.extend)
    else:
        while True:
            text = input("Dime:")
            if len(text) == 0:
                break
            results = search(text, index)
            print_results(results, args.extend)
                    

