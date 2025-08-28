def test_google_search(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title, "Google title is not found"