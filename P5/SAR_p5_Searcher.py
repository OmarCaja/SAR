#!/usr/bin/env python

from whoosh.index import open_dir
from whoosh.qparser import QueryParser

if __name__ == "__main__":
    ix = open_dir("index_dir")
    with ix.searcher() as searcher:
        while True:
            text = input("Dime:")
            if len(text) == 0:
                break
            query = QueryParser("content", ix.schema).parse(text)
            results = searcher.search(query)
            for r in results:
                print(r)

