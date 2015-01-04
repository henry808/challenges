#!/usr/bin/env python

"""
code that tests library_renderer.py module

can be run with py.test
"""

import cStringIO

import pytest  # used for the exception testing

import library as lb


def test_book_init():
    """Test Book class constructor

    Test with a title and with no title.
    """
    b1 = lb.Book('The Spam and Spam')
    assert isinstance(b1, lb.Book)
    assert repr(b1) == "Book('The Spam and Spam')"
    b2 = lb.Book()
    assert isinstance(b2, lb.Book)
    assert repr(b2) == "Book('')"


def test_book_enshelf():
    """Test Book class enshelf method

    Test creating a shelf and putting three books on it and
        a 4th book on a different shelf.
    Test to make sure that each book knows what shelf it is on
    """
    b1 = lb.Book('The Trueth Behind Spam')
    b2 = lb.Book('The War and Pieces of Spam')
    b3 = lb.Book('Cheeze and Spam')
    b4 = lb.Book('From Russia with Spam')
    s1 = lb.Shelf('Epics')
    s2 = lb.Shelf('Espionage')
    b1.enshelf(s1)
    b2.enshelf(s1)
    b3.enshelf(s1)
    b4.enshelf(s2)

    # make sure books know what shelves they are on.
    assert b1.shelf == s1
    assert b2.shelf == s1
    assert b3.shelf == s1
    assert b4.shelf == s2


def test_shelved_book_enshelf():
    """Test Book class enshelf method when book is on another shelf

    Test moving books from one shelf to another.
    Test to make sure that each book knows it moved to the right shelf
    """
    b1 = lb.Book('The Trueth Behind Spam')
    b2 = lb.Book('The War and Pieces of Spam')
    b3 = lb.Book('Cheeze and Spam')
    b4 = lb.Book('From Russia with Spam')
    s1 = lb.Shelf('Old Shelf')
    s2 = lb.Shelf('New Shelf')
    b1.enshelf(s1)
    b2.enshelf(s1)
    b3.enshelf(s1)
    b4.enshelf(s1)
    # move to new shelf
    b1.enshelf(s2)
    b2.enshelf(s2)
    b3.enshelf(s2)
    b4.enshelf(s2)

    # make sure books know they moved to new shelf.
    assert b1.shelf == s2
    assert b2.shelf == s2
    assert b3.shelf == s2
    assert b4.shelf == s2


def test_book_unshelf():
    """Test Book class enshelf method

    Test creating a shelf and putting three books on it and
        a 4th book on a different shelf.
    Test to make sure that each book knows what shelf it is on
    """
    b1 = lb.Book('The Trueth Behind Spam')
    b2 = lb.Book('The War and Pieces of Spam')
    b3 = lb.Book('Cheeze and Spam')
    b4 = lb.Book('From Russia with Spam')
    s1 = lb.Shelf('Epics')
    b1.enshelf(s1)
    b2.enshelf(s1)
    b3.enshelf(s1)
    b4.enshelf(s1)
    b2.unshelf()
    b3.unshelf()

    # make sure books know what shelves they are on.
    assert b1.shelf == s1
    assert b2.shelf is None
    assert b3.shelf is None
    assert b4.shelf == s1


def test_shelf_init():
    """Test Shelf class constructor

    Test with a name and without a name.
    """
    s1 = lb.Shelf('Books on Foods')
    assert isinstance(s1, lb.Shelf)
    assert repr(s1) == "Shelf('Books on Foods')"
    s2 = lb.Shelf()
    assert isinstance(s1, lb.Shelf)
    assert repr(s2) == "Shelf('')"


def test_shelf_init_booklist():
    """Test Shelf class constructor

    Test adding a list of books.
    """
    b1 = lb.Book('The Trueth Behind Spam')
    b2 = lb.Book('The War and Pieces of Spam')
    b3 = lb.Book('Cheeze and Spam')
    b4 = lb.Book('From Russia with Spam')
    s1 = lb.Shelf('Books', [b1, b2, b3, b4])
    compare = "Shelf('Books', [{}, {}, {}, {}])".format(b1, b2, b3, b4)
    assert isinstance(s1, lb.Shelf)
    assert repr(s1) == compare



def test_shelf_for_book_enshelf():
    """Test Shelf class when Book class enshelf method used

    Test creating a shelf and putting three books on it and
        a 4th book on a different shelf.
    Test to make sure that each shelf knows what books are on it.
    """
    b1 = lb.Book('The Trueth Behind Spam')
    b2 = lb.Book('The War and Pieces of Spam')
    b3 = lb.Book('Cheeze and Spam')
    b4 = lb.Book('From Russia with Spam')
    s1 = lb.Shelf('Epics')
    s2 = lb.Shelf('Espionage')
    b1.enshelf(s1)
    b2.enshelf(s1)
    b3.enshelf(s1)
    b4.enshelf(s2)

    # make sure books know what shelves they are on.
    compare1 = "Shelf('Epics', [{}, {}, {}])".format(b1, b2, b3)
    compare2 = "Shelf('Espionage', [{}])".format(b4)
    assert repr(s1) == compare1
    assert repr(s2) == compare2


def test_shelf_for_book_unshelf():
    """Test Shelf class enshelf method

    Test creating a shelf and putting four books on it and
        then removing two of them
    Make sure shelf has the remaining two books on it.
    """
    b1 = lb.Book('The Trueth Behind Spam')
    b2 = lb.Book('The War and Pieces of Spam')
    b3 = lb.Book('Cheeze and Spam')
    b4 = lb.Book('From Russia with Spam')
    s1 = lb.Shelf('Epics')
    b1.enshelf(s1)
    b2.enshelf(s1)
    b3.enshelf(s1)
    b4.enshelf(s1)
    b2.unshelf()
    b3.unshelf()

    # make sure shelf has two books left on it.
    compare = "Shelf('Epics', [{}, {}])".format(b1, b4)
    assert repr(s1) == compare


def test_shelves_shelved_book_enshelf():
    """Test Shelf for book class enshelf method when book is reshelved

    Test moving books from one shelf to another.
    Test to make sure that each book is moved properly from shelf to shelf
    """
    b1 = lb.Book('The Trueth Behind Spam')
    b2 = lb.Book('The War and Pieces of Spam')
    b3 = lb.Book('Cheeze and Spam')
    b4 = lb.Book('From Russia with Spam')
    s1 = lb.Shelf('Old Shelf')
    s2 = lb.Shelf('New Shelf')
    b1.enshelf(s1)
    b2.enshelf(s1)
    b3.enshelf(s1)
    b4.enshelf(s1)
    # move to new shelf
    b1.enshelf(s2)
    b2.enshelf(s2)
    b3.enshelf(s2)
    b4.enshelf(s2)

    # make sure books know they moved to new shelf.
    compare1 = "Shelf('Old Shelf', [])"
    compare2 = "Shelf('New Shelf', [{}, {}, {}, {}])".format(b1, b2, b3, b4)
    assert repr(s1) == compare1
    assert repr(s1) == compare2


    # test str and repr
