import os


def get_project_name():
    for folder_name, sub_folder, file_name in os.walk("D:\\Code"):
        print(folder_name)
        print(sub_folder)


if __name__ == "__main__":
    get_project_name()
