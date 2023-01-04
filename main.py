import os
from pathlib import Path


def image_format_changer(folder_path):
    file_list = os.listdir(folder_path)
    for file in file_list:
        file_path = Path.joinpath(folder_path, file)
        file_name = file_path.stem
        extracted_path = Path.joinpath(folder_path, "extracted")
        extracted_path.mkdir(parents=True, exist_ok=True)
        rename_file_name = f"{file_name}.jpg"
        rename_file_path = Path.joinpath(extracted_path, rename_file_name)
        os.rename(file_path, rename_file_path)
        print(rename_file_name)


def main():
    folder_path = Path(r"D:\WorkStation\Drama-Zone\Pinterest\test")
    image_format_changer(folder_path=folder_path)


if __name__ == "__main__":
    main()
