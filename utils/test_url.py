from url import extract_category_name

def test_extract_category_name():
    # Arrange
    url =  "http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html"
    expected = "nonfiction_13"
    
    # Act
    actual = extract_category_name(url)

    # Assert
    assert(actual == expected)
