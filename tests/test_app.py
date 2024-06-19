from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===

def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        "Title: Doolittle Released: 1989",
        "Title: Surfer Rosa Released: 1988",
        "Title: Waterloo Released: 1974",
        "Title: Super Trouper Released: 1980",
        "Title: Bossanova Released: 1990",
        "Title: Lover Released: 2019",
        "Title: Folklore Released: 2020",
        "Title: I Put a Spell on You Released: 1965",
        "Title: Baltimore Released: 1978",
        "Title: Here Comes the Sun Released: 1971",
        "Title: Fodder on My Wings Released: 1982",
        "Title: Ring Ring Released: 1973"
    ])

# Adding links for the album detail page.

def test_visit_album_show_detail_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Album Detail")
    paragraph_tag = page.locator("p")
    expect(paragraph_tag).to_have_text("Released: 1988")


def test_visit_album_show_page_and_go_back (page, test_web_address):
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'")
    page.click("text=' Go back to album list'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")

# def test_get_list_of_artists

def test_get_artist_listing(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")

    # We look at all the div tags
    div_tags = page.locator("div")

    # We assert that it has the artists in it
    expect(div_tags).to_have_text([
        "Name: Pixies",
        "Name: ABBA",
        "Name: Taylor Swift",
        "Name: Nina Simone"
    ])


    '''
    "Name : Pixies Genre: Rock",
        "Name : ABBA Genre: Pop",
        "Name : Taylor Swift Genre: Pop",
        "Name : Nina Simone Genre: Jazz"
    '''