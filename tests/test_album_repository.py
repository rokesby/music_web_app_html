from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""

def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new ArtistRepository

    albums = repository.all() # Get all albums

    # Assert on the results
    assert albums == [
        Album('Doolittle', 1989, 1,1),
        Album('Surfer Rosa', 1988, 1,2),
        Album('Waterloo', 1974, 2,3),
        Album('Super Trouper', 1980, 2,4),
        Album('Bossanova', 1990, 1,5),
        Album('Lover', 2019,3,6),
        Album('Folklore', 2020, 3,7),
        Album('I Put a Spell on You', 1965, 4,8),
        Album('Baltimore', 1978, 4,9),
        Album('Here Comes the Sun', 1971, 4,10),
        Album('Fodder on My Wings', 1982, 4,11),
        Album('Ring Ring', 1973, 2, 12)
    ]

"""
When we call ArtistRepository#find
We get a list of albums for a specific artist.
"""
def test_get_two_records(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    albums = repository.find(2)
    assert albums == [
        Album('Waterloo', 1974, 2, 3),
        Album('Super Trouper', 1980, 2, 4),
        Album('Ring Ring', 1973, 2, 12)
    ]
"""
When we call ArtistRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album('The Comeback', 2024, 2))
    repository.create(Album('Rockstar', 2021, 5))

    result = repository.all()
    assert result == [
        Album('Doolittle', 1989, 1,1),
        Album('Surfer Rosa', 1988, 1,2),
        Album('Waterloo', 1974, 2,3),
        Album('Super Trouper', 1980, 2,4),
        Album('Bossanova', 1990, 1,5),
        Album('Lover', 2019,3,6),
        Album('Folklore', 2020, 3,7),
        Album('I Put a Spell on You', 1965, 4,8),
        Album('Baltimore', 1978, 4,9),
        Album('Here Comes the Sun', 1971, 4,10),
        Album('Fodder on My Wings', 1982, 4,11),
        Album('Ring Ring', 1973, 2, 12),
        Album('The Comeback', 2024, 2, 13),
        Album('Rockstar', 2021, 5, 14)
    ]

"""
When we call ArtistRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(3) # Apologies to Taylor Swift fans

    result = repository.all()
    assert result == [
        Album('Doolittle', 1989, 1,1),
        Album('Surfer Rosa', 1988, 1,2),
        Album('Waterloo', 1974, 2,3),
        Album('Super Trouper', 1980, 2,4),
        Album('Bossanova', 1990, 1,5),
        Album('I Put a Spell on You', 1965, 4,8),
        Album('Baltimore', 1978, 4,9),
        Album('Here Comes the Sun', 1971, 4,10),
        Album('Fodder on My Wings', 1982, 4,11),
        Album('Ring Ring', 1973, 2, 12)
    ]


def test_get_specific_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    myAlbum = repository.get_album_specific(9)
    assert myAlbum == Album('Baltimore', 1978, 4)
    