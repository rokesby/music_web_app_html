import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

from lib.album_repository import AlbumRepository
from lib.album import Album


from lib.artist_repository import ArtistRepository, Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')


# GET /albums
# Produces a list of albums for a web site.
'''
Query the album repository and retrieve an album object
Send the album object to a templated file and cycle through it
Unsure of how to test the final output... maybe with playwright?
'''
@app.route('/albums', methods=['GET'])
def get_albums():
    Connection = get_flask_database_connection(app)
    repository = AlbumRepository(Connection)
    albums = repository.all()
    return render_template('albums.html', albums=albums)


# Now using a path parameter.....
@app.route('/albums/<id>')
def get_album_specific(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.get_album_specific(id)
    return render_template('album_specific.html', album=album)


# POST /albums
# Stores a new album.
@app.route('/albums',methods=['POST'])
def post_albums():

    if has_invalid_album_parameters(request.form):
        return "No album details provided.", 400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    new_album = Album(request.form['title'], request.form['release_year'], request.form['artist_id'])
    repository.create(new_album)        
    return "", 200



def has_invalid_album_parameters(form):
    return 'title' not in form or \
        'release_year' not in form or \
        'artist_id' not in form


# Artists lists
@app.route('/artists', methods=['GET'])
def get_artist_list():
    Connection = get_flask_database_connection(app)
    repository = ArtistRepository(Connection)
    artists = repository.all()
    return render_template('artists.html', artists = artists)


# Now using a path parameter.....Artist detail
@app.route('/artists/<id>')
def get_artist_specific(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    my_artist = repository.find(id)
    return render_template('artist_specific.html', my_artist=my_artist)

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
