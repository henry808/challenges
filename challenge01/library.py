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
            shelf.add_book(self)
            pass
        # self.shelf = shelf

    def unshelf(self):
        """Removes the book from its shelf
        """
        if self.shelf:
            # remove book from shelf
            self.shelf.remove_book(self)
        self.shelf = None

    def __str__(self):
        """str representation of Book object
        """
        return "Book: {}".format(self.title)

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
        for book in self.books:
            book.shelf = self
        super(Shelf, self).__init__()

    def add_book(self, book):
        """Add a book to this shelf
        """
        self.books.append(book)
        book.shelf = self

    def remove_book(self, book):
        """Remove a book from this shelf
        """
        self.books.remove(book)
        book.shelf = None

    def __str__(self):
        """str representation of Shelf object
        """
        text = "Shelf {} contains {}"
        books = [str(book) for book in self.books]
        return text.format(self.shelf_name, books)

    def __repr__(self):
        """str representation of Shelf object
        """
        books = str(self.books)
        # strip brackets off list
        books = books[1:-1]
        # if any books, then need to put a comma before them
        if books:
            books = ", {}".format(books)
        return 'Shelf(\'{}\'{})'.format(self.shelf_name, books)


class Library(object):
    """A Library object.

    A class representing a library containing shelves containing books.
    """
    def __init__(self, library_name='', *args):
        self.library_name = library_name
        self.shelves = list(args)
        super(Library, self).__init__()

    def add_shelf(self, shelf):
        """Add a shelf from this library
        """
        self.shelves.append(shelf)

    def remove_shelf(self, shelf):
        """Remove a shelf from this library
        """
        self.shelves.remove(shelf)

    def book_list(self):
        """Return a list of all books in this library
        """
        books = []
        for shelf in self.shelves:
            for book in shelf.books:
                books.append(book)
        return books

    def __str__(self):
        """str representation of library object
        """
        text = "Library {} contains shelves {}"
        shelves = [str(shelf) for shelf in self.shelves]
        return text.format(self.library_name, shelves)

    def __repr__(self):
        """str representation of library object
        """
        shelves = str(self.shelves)
        # strip brackets off list
        shelves = shelves[1:-1]
        # if any shelves, then need to put a comma before them
        if shelves:
            shelves = ", {}".format(shelves)
        return 'Library(\'{}\'{})'.format(self.library_name, shelves)


if __name__ == '__main__':
    books = [Book('The Truth of Spam'),
             Book('Of Mice and Spam'),
             Book('The Spam'),
             Book('The Eggs'),
             Book('Tales of Spam')]

    print('Books:')
    for book in books:
        print(book)
    print('\n')

    s1 = Shelf('First', books[0], books[1])
    s2 = Shelf('Second')
    books[2].enshelf(s2)
    books[3].enshelf(s2)
    s2.add_book(books[4])
    s3 = Shelf('Empty')

    print('Shelves:')
    print(s1)
    print(s2)
    print('\n')

    print('Books on shelves:')
    text = "Book {} is on shelf: {}."
    for book in books:
        print(text.format(book.title, book.shelf.shelf_name))
    print('\n')

    print('Show repr of Shelves:')
    print(repr(s1))
    print(repr(s2))
    print(repr(s3))
    print('\n')

    l = Library('Uptown', s1, s2, s3)
    print('Show the library:')
    print(repr(l))
    print('\n')

    print('Print the library:')
    print(l)
    print('\n')

    print('List of all books in the library:')
    for book in l.book_list():
        print(book)
    print('\n')

    l2 = Library('Uptown', Shelf('First', Book('The Spam and Spam'), Book('')),
                 Shelf('Second', Book('The Spam'), Book('The Eggs'),
                 Book('Tales of Spam')), Shelf('Empty'))

    print('Set a second library:')
    print(repr(l2))
