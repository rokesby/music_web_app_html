from lib.album import Album

import pytest


'''
Good album
'''
def test_is_album_valid_good():
    newAlbum = Album('Album title', 1999, 3)
    assert newAlbum.is_album_valid()


''' Bad album with no title
'''
def test_is_album_valid_bad_title():

    newAlbum = Album('', 0, 3)
    assert newAlbum.is_album_valid() == False

    newAlbum2 = Album(None, 0, 3)
    assert newAlbum2.is_album_valid() == False

def test_is_album_valid_bad_release():

    newAlbum = Album('My title', '', 3)
    assert newAlbum.is_album_valid() == False

    newAlbum3 = Album("My title", None, 3)
    assert newAlbum3.is_album_valid() == False


'''
Test error returns when bad parameters are passed

'''

def test_error_messages():
    myAlbum1 = Album("", '', 3)
    assert myAlbum1.generate_errors() == [
        "Title must not be blank",
        "Release year must not be blank"
    ]

    myAlbum2 = Album("Title", '', 3)
    assert myAlbum2.generate_errors() == [
        "Release year must not be blank"
    ]

    myAlbum3 = Album("", 1999, 3)
    assert myAlbum3.generate_errors() == [
        "Title must not be blank"
    ]

"""

"""

def test_get_valid_title():
    myAlbum1 = Album("Title", 1999, 3)
    assert myAlbum1.get_valid_title() == "Title"

def test_get_valid_title_if_title_valid():
    myAlbum1 = Album("Title", 1999, 3)
    assert myAlbum1.get_valid_title() == "Title"

def test_get_valid_title_if_title_invalid():
    myAlbum1 = Album("", 1999, 3)
    with pytest.raises(ValueError) as err:
        myAlbum1.get_valid_title()
    assert str(err.value) == "Cannot get valid title"



def test_get_valid_release_if_release_valid():
    myAlbum1 = Album("Title", 1999, 3)
    assert myAlbum1.get_valid_release_year() == 1999

def test_get_valid_release_if_release_invalid():
    myAlbum1 = Album("Title", "", 3)
    with pytest.raises(ValueError) as err:
        myAlbum1.get_valid_release_year()
    assert str(err.value) == "Cannot get valid release year"