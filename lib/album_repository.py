from lib.album import Album

class AlbumRepository():

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["title"], row["release_year"], row["artist_id"], row["id"])
            albums.append(item)
        return albums
    

    def create(self, Album):
        self._connection.execute(
            'INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', 
            [Album.title, int(Album.release_year), int(Album.artist_id)])
        return None


 # Find albums by their artist id
    def find(self, artist_id):
        albums= []
        rows = self._connection.execute(
            'SELECT * from albums WHERE artist_id = %s', [artist_id])
        for row in rows:
            item = Album(row["title"], row["release_year"], row["artist_id"], row["id"])
            albums.append(item)
        return albums

    # Create a new album
    # Do you want to get its id back? Look into RETURNING id;
    # def create(self, album):
    #     self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [album.title, album.release_year, album.artist_id])
    #     return None

    # Delete an artist by their id
    def delete(self, artist_id):
        self._connection.execute(
            'DELETE FROM albums WHERE artist_id = %s', [artist_id])
        return None

    def get_album_specific(self, album_id):
        rows = self._connection.execute('select * from albums where id = %s', [album_id])
        for row in rows: # Should be only 1 row returned.
            album = Album(row["title"], row["release_year"], row["artist_id"])
        return album