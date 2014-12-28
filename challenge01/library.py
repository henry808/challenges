#!/usr/bin/env python

# library.py
"""
Library package

This is a package with classes that represent a Library, Shelves, and Books


"""
from __future__ import print_function


class Book(object):
    """A Book object.

    A class representing books in a Library.
    """
    def __init__(self, shelf=None, **kwargs):
        self.title = ''
        self.shelf = None
        self.attributes = kwargs
        super(Book, self).__init__()


    def enshelf(self, shelf):
        """Put the book on a shelf
        """
        if shelf:
            # add book to shelf
            shelf.addbook
            pass
        self.shelf = shelf


    def unshelf(self):
        """Removes the book from its shelf
        """
        if self.shelf:
            # remove book from shelf
            self.shelf.remove
            pass        
        self.shelf = None

class Shelf(object):
    """A Shelf object.

    A class representing shelves containing books in a Library.
    """
    def __init__(self):
        self.books = []
        super(Shelf, self).__init__()


if __name__ == '__main__':
    pass
