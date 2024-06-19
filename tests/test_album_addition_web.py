from playwright.sync_api import Page, expect



def test_create_album(page, test_web_address, db_connection):
    
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click('text="Add album"')

    page.fill('input[name=title]', "Test album")
    page.fill('input[name=release_year]', "1234")
    page.click('text="Add album"')

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Album Detail")
    
    paragraph_tag = page.locator("p")
    expect(paragraph_tag).to_have_text("Released: 1234")



def test_validate_album_entry(page, test_web_address, db_connection):
    
    page.set_default_timeout(1000)
    # fill out with insufficient information.
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click('text="Add album"')
    page.click('text="Add album"')

    errors_tag = page.locator(".t-errors")
    expect (errors_tag).to_have_text("Your submission contains errors: ['Title must not be blank', 'Release year must not be blank']")
