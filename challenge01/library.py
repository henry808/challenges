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
    def __init__(self, title='', shelf=None, content=''):
        self.title = title
        self.shelf = shelf
        self.content = content
        super(Book, self).__init__()

    def enshelf(self, shelf):
        """Put the book on a shelf
        """
        if self.shelf:
            # remove book from old shelf
            self.unshelf()
        if shelf:
            # add book to shelf
            shelf.addbook(self)
            pass
        # self.shelf = shelf

    def unshelf(self):
        """Removes the book from its shelf
        """
        if self.shelf:
            # remove book from shelf
            self.shelf.remove(self)
        self.shelf = None

    def __str__(self):
        """str representation of Book object
        """
        return "Book with title: {}".format(self.title)

    def __repr__(self):
        """str representation of Book object
        """
        return 'Book(\'{}\')'.format(self.title)


class Shelf(object):
    """A Shelf object.

    A class representing shelves containing books in a Library.
    """
    def __init__(self, shelf_name='', *args):
        self.shelf_name = shelf_name
        self.books = list(args)
        if args:
            self.books 
        super(Shelf, self).__init__()

    def addbook(self, book):
        """Add a book to this shelf
        """
        self.books.append(book)
        book.shelf = self

    def remove(self, book):
        """Remove a book from this shelf
        """
        self.books.remove(book)
        book.shelf = None

    def __str__(self):
        """str representation of Shelf object
        """
        text = "Shelf with name: {} containing books {}"
        return text.format(self.shelf_name, self.books)

    def __repr__(self):
        """str representation of Shelf object
        """
        print(self.books)

        books = str(self.books)
        return 'Shelf(\'{}\', [{}])'.format(self.shelf_name, books)


class Library(object):
    """A Library object.

    A class representing a library containing shelves containing books.
    """
    def __init__(self, library_name=''):
        self.library_name = library_name
        self.shelves = []
        super(Library, self).__init__()

    def __str__(self):
        """str representation of library object
        """
        text = "Library with name: {} containing shelves {}"
        return text.format(self.library_name, self.shelf_name)

    def __repr__(self):
        """str representation of Book object
        """
        return 'Library({})'.format(self.library_name)

if __name__ == '__main__':
    b1 = Book('The Spam and Spam')
    b2 = Book()
    b3 = Book('The Spam')
    b4 = Book('The Eggs')

    print(b1)
    print(b2)
    print(b3)

    l = [b1, b2, b3]

    print(l)

    s = Shelf('First Shelf', b1)

    print(s)

    # b1.enshelf(s)
    # b2.enshelf(s)
    # b3.enshelf(s)

    # print(b1.shelf)
    # print(b2.shelf)
    # print(b3.shelf)
    # print(b3.shelf)
    # print(b4.shelf)

    print(repr(s))
