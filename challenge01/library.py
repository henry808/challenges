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
    def __init__(self, title='', shelf=None, **kwargs):
        self.title = title
        self.shelf = shelf
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
        self.shelf = None

    def __str__(self):
        """str representation of Book object
        """
        return "Book with title: {}".format(self.title)

    def __repr__(self):
        """str representation of Book object
        """
        return 'Book({})'.format(self.title)


class Shelf(object):
    """A Shelf object.

    A class representing shelves containing books in a Library.
    """
    def __init__(self, shelf_name=''):
        self.shelf_name = shelf_name
        self.books = []
        super(Shelf, self).__init__()

    def __str__(self):
        """str representation of shelfobject
        """
        text = "Shelf with name: {} containing books {}"
        return text.format(self.shelf_name, self.books)

    def __repr__(self):
        """str representation of Book object
        """
        return 'Shelf({})'.format(self.shelf_name)


class Library(object):
    """A Library object.

    A class representing a library containing shelves containing books.
    """
    def __init__(self):
        self.books = []
        super(Shelf, self).__init__()

if __name__ == '__main__':
    b1 = Book('The Spam and Spam')
    b2 = Book()
    b3 = Book('The Spam')

    print(b1)
    print(b2)
    print(b3)
