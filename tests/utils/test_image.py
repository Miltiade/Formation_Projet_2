from image import download
import os

def test_it_downloads_an_image():
    #Arrange
    url = "https://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg"    
    #Act
    download(url)
    #Assert
    assert(True == os.path.isfile("images/fe72f0532301ec28892ae79a629a293c.jpg"))
