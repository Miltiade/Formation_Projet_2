def extract_category_name(url):
    return url.split("/")[-2]


def extract_image_name_from_url(url):
    return url.split("/")[-1]
