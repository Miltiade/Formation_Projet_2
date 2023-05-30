"""A script to create directory: output_files"""

from pathlib import Path


def create_output_files_directory():
    base_directory = Path("output_files")
    base_directory.mkdir(parents=True, exist_ok=True)
    return "directory created successfully!"


# TEST DE LA FONCTION DEFINIE CI-DESSUS:
# result = create_output_files_directory()
# print(result)
