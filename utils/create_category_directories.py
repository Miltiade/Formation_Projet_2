"""A script to create directories: 
-- /output_files/category_sequential_art/
-- /output_files/category_sequential_art/images"""

from pathlib import Path

def create_category_directories():
    base_directory = Path("output_files")
    sequential_art_directory = base_directory / "category_sequential_art"
    sequential_art_directory.mkdir(parents=True, exist_ok=True)
    sequential_art_images_directory = sequential_art_directory / "images"
    sequential_art_images_directory.mkdir(parents=True, exist_ok=True)
    return "directories created successfully!"

# TEST DE LA FONCTION DEFINIE CI-DESSUS:
# result = create_category_directories()
# print(result)