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
    
    def is_album_valid(self):
        
        if self._is_title_invalid():
            return False
        
        if self._is_release_invalid():
            return False
        
        return True
    
    def generate_errors(self):
        errors = []
        if self._is_title_invalid():
            errors.append("Title must not be blank")
        if self._is_release_invalid():
            errors.append("Release year must not be blank")
        return errors

    def _is_title_invalid(self):
        if self.title is None:
            return True
        if self.title == "":
            return True
        else:
            return False
        
    def _is_release_invalid(self):
        if self.release_year is None:
            return True
        if self.release_year == "":
            return True
        else:
            return False
        
    def get_valid_title(self):
        if self._is_title_invalid():
            raise ValueError("Cannot get valid title")
        return self.title
    

    def get_valid_release_year(self):
        if self._is_release_invalid():
            raise ValueError("Cannot get valid release year")
        return self.release_year
    # just changed this.