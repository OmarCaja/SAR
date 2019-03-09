#!/usr/bin/env python

from whoosh.index import open_dir
from whoosh.qparser import QueryParser
import argparse
import json

def syntax():
    return "python SAR_p5_Searcher.py index_directory [-q=query] [--extend]"

def search_and_print(text, index, extended):
    with index.searcher() as searcher:
        query = QueryParser("article", index.schema).parse(text)
        results = searcher.search(query)
        print_results(results, extended)

def print_default(results):
    for result in results:
        date = result["date"]
        title = result["title"]
        keywords = result["keywords"]
        print("-> (%s) %s (%s)" %(date, title, keywords))

def print_extended(results):
    for result in results:
        date = result["date"]
        title = result["title"]
        keywords = result["keywords"]
        path = result["path"]
        article = get_file_article(path)
        print("")
        print("Title: " + title)
        print("Date: " + date)
        print("Keywords " + keywords)
        print("")
        print(article)

def get_file_article(filename):
    with open(filename, "r") as fh:
        return json.load(fh)["article"]

def print_results(results, extended):
    if extended:
        print_extended(results)
    else:
        print_default(results)
    print("=================")
    print(str(len(results)) + " results")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(usage=syntax())
    parser.add_argument("index", help="index directory")
    parser.add_argument("-q", help="query to search")
    parser.add_argument("--extend", action="store_true", help="indicates if you want all the information")

    args = parser.parse_args()

    index = open_dir(args.index)
    
    if args.q:
        search_and_print(args.q, index, args.extend)
    else:
        while True:
            text = raw_input("Dime: ")
            if len(text) == 0:
                break
            search_and_print(text, index, args.extend)
                    

