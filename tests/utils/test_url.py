from url import extract_category_name, extract_image_name_from_url

def test_extract_category_name():
    # Arrange
    url =  "http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html"
    expected = "nonfiction_13"
    # Act
    actual = extract_category_name(url)
    # Assert
    assert(actual == expected)

def test_it_extracts_image_name_from_url():
    # Arrange
    url =  "https://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg"
    expected = "fe72f0532301ec28892ae79a629a293c.jpg"    
    # Act
    actual = extract_image_name_from_url(url)
    # Assert
    assert(actual == expected)