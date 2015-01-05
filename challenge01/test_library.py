#!/usr/bin/env python

"""
code that tests library_renderer.py module

can be run with py.test
"""

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
    s1 = lb.Shelf('Books', b1, b2, b3, b4)
    shelf_string = "Shelf('Books', {}, {}, {}, {})"
    compare = shelf_string.format(repr(b1), repr(b2), repr(b3), repr(b4))
    assert isinstance(s1, lb.Shelf)
    assert repr(s1) == compare


def test_shelf_init_booklist_then_add_books():
    """Test Shelf class constructor

    Test adding a list of books, then adding a couple books with enshelf
    """
    b1 = lb.Book('The Trueth Behind Spam')
    b2 = lb.Book('The War and Pieces of Spam')
    b3 = lb.Book('Cheeze and Spam')
    b4 = lb.Book('From Russia with Spam')
    s1 = lb.Shelf('Books', b1, b2)
    b3.enshelf(s1)
    b4.enshelf(s1)
    shelf_string = "Shelf('Books', {}, {}, {}, {})"
    compare = shelf_string.format(repr(b1), repr(b2), repr(b3), repr(b4))
    assert isinstance(s1, lb.Shelf)
    assert repr(s1) == compare


def test_shelf_remove():
    """Test remeving books from a shelf

    Test adding four books and then removing two of them with remove method
    """
    b1 = lb.Book('The Trueth Behind Spam')
    b2 = lb.Book('The War and Pieces of Spam')
    b3 = lb.Book('Cheeze and Spam')
    b4 = lb.Book('From Russia with Spam')
    s1 = lb.Shelf('Books', b1, b2, b3, b4)
    s1.remove_book(b2)
    s1.remove_book(b3)
    shelf_string = "Shelf('Books', {}, {})"
    compare = shelf_string.format(repr(b1), repr(b4))
    assert isinstance(s1, lb.Shelf)
    assert repr(s1) == compare


def test_shelf_remove_twice():
    """Test removing books from a shelf

    Tests removing the same book twice.
    """
    b1 = lb.Book('The Trueth Behind Spam')
    b2 = lb.Book('The War and Pieces of Spam')
    b3 = lb.Book('Cheeze and Spam')
    b4 = lb.Book('From Russia with Spam')
    s1 = lb.Shelf('Books', b1, b2, b3, b4)
    s1.remove_book(b2)
    s1.remove_book(b3)
    with pytest.raises(ValueError):
        s1.remove_book(b2)
    shelf_string = "Shelf('Books', {}, {})"
    compare = shelf_string.format(repr(b1), repr(b4))
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
    comp1 = "Shelf('Epics', {}, {}, {})".format(repr(b1), repr(b2), repr(b3))
    comp2 = "Shelf('Espionage', {})".format(repr(b4))
    assert repr(s1) == comp1
    assert repr(s2) == comp2


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
    compare = "Shelf('Epics', {}, {})".format(repr(b1), repr(b4))
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
    compare1 = "Shelf('Old Shelf')"
    shelf_string = "Shelf('New Shelf', {}, {}, {}, {})"
    compare2 = shelf_string.format(repr(b1), repr(b2), repr(b3), repr(b4))
    assert repr(s1) == compare1
    assert repr(s2) == compare2


def test_library_init():
    """Test Library class constructor

    Test putting shelves with books into a library
    """
    l = lb.Library('Uptown',
                   lb.Shelf('First', lb.Book('The Spam and Spam'),
                            lb.Book('')),
                   lb.Shelf('Second', lb.Book('The Spam'),
                            lb.Book('The Eggs'), lb.Book('Tales of Spam')),
                   lb.Shelf('Empty'))

    text1 = "Library('Uptown', Shelf('First', Book('The Spam and Spam')"
    text2 = ", Book('')), Shelf('Second', Book('The Spam'), Book('The Eggs'),"
    text3 = " Book('Tales of Spam')), Shelf('Empty'))"

    compare = "".join([text1, text2, text3])

    assert isinstance(l, lb.Library)
    assert repr(l) == compare


def test_library_add_shelf():
    """Test Library class add_shelf method
    """
    b1 = lb.Book('The Trueth Behind Spam')
    b2 = lb.Book('The War and Pieces of Spam')
    b3 = lb.Book('Cheeze and Spam')
    b4 = lb.Book('From Russia with Spam')
    b5 = lb.Book('Sir Spamalot')
    s1 = lb.Shelf('Epics', b1, b2, b3)
    s2 = lb.Shelf('Espionage', b4)
    s3 = lb.Shelf('Medieval', b5)
    l1 = lb.Library('Seattle', s1, s2)
    l1.add_shelf(s3)

    compare = lb.Library('Seattle', s1, s2, s3)

    assert isinstance(l1, lb.Library)
    assert repr(l1) == repr(compare)


def test_library_remove_shelf():
    """Test Library class remove_shelf method
    """
    b1 = lb.Book('The Trueth Behind Spam')
    b2 = lb.Book('The War and Pieces of Spam')
    b3 = lb.Book('Cheeze and Spam')
    b4 = lb.Book('From Russia with Spam')
    b5 = lb.Book('Sir Spamalot')
    s1 = lb.Shelf('Epics', b1, b2, b3)
    s2 = lb.Shelf('Espionage', b4)
    s3 = lb.Shelf('Medieval', b5)
    l1 = lb.Library('Seattle', s1, s2, s3)
    l1.remove_shelf(s3)

    compare = lb.Library('Seattle', s1, s2)

    assert isinstance(l1, lb.Library)
    assert repr(l1) == repr(compare)


def test_library_book_list():
    """Test Library class book_list method

    Test to make sure book list lists all books in the library.
    """
    b1 = lb.Book('The Trueth Behind Spam')
    b2 = lb.Book('The War and Pieces of Spam')
    b3 = lb.Book('Cheeze and Spam')
    b4 = lb.Book('From Russia with Spam')
    b5 = lb.Book('Sir Spamalot')
    s1 = lb.Shelf('Epics', b1, b2, b3)
    s2 = lb.Shelf('Espionage', b4)
    s3 = lb.Shelf('Medieval', b5)
    l1 = lb.Library('Seattle', s1, s2, s3)

    all_books = [b1, b2, b3, b4, b5]

    assert isinstance(l1, lb.Library)
    assert l1.book_list() == all_books
