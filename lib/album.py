class Album():
    def __init__(self, title, release_year, artist_id, album_id=None):
        self.artist_id = artist_id
        self.title = title
        self.release_year = release_year
        self.album_id = album_id


    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__