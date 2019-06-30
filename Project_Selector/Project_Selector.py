#! python3.7

from git import Repo
import os
import subprocess

project_dictionary = {}


def get_project_name(project_directory="D:\\Code"):
    # function to read all the projects within my code directory
    # and to assign them to a dictionary
    return_dictionary = {}
    project_names = os.listdir(project_directory)

    for name in project_names:
        return_dictionary[name] = os.path.join(project_directory, name)

    return return_dictionary


def enter_project_name():
    # function which will take in a project name and direct the system to
    # the associated folder
    while True:
        name_entry = input("Please enter project you wish to work on: ")
        try:
            return project_dictionary[name_entry]
        except KeyError:
            list_projects()


def list_projects():
    # function to project a listing of all projects
    print("Available Projects are: ")
    for p in project_dictionary:
        print(p)


def checkout_branch():
    # function to provide all the available local branches
    r = Repo()
    repo_heads = r.heads
    head_names = [h.name for h in repo_heads]

    if len(head_names) == 1:
        print(f"Only the {head_names[0]} branch exists - checking it out")
        return repo_heads[head_names[0]].checkout()
    else:
        while True:
            print("Available branches are: ")
            for h in head_names:
                print(h)
            branch = input("Enter branch you want to work on: ")
            try:
                repo_heads[branch].checkout()
                break
            except KeyError:
                print("Invalid Branch - input is case-sensitive")


# def ide_opener():
    # while True:
    #     ide_checker = input("Do you want to open an IDE? ")
    #     if ide_checker == 'N':
    #         break
    #     else:
    #         which_ide = input("Do you want to open -(A)tom, (P)ycharm or (I)ntellij? ")
    #         if which_ide.upper() is not 'A' or not 'P' or not 'I':
    #             print("Please try again")
    #         elif which_ide.upper() == 'A':
    #             os.system("atom")
    #             break
    #         elif which_ide.upper() == 'P':
    #             subprocess.call("pycharm")


if __name__ == "__main__":
    project_dictionary = get_project_name()
    if len(project_dictionary) > 1:
        list_projects()
    else:
        project_key = project_dictionary.keys()
        print(f"Only Project {project_key} exists")
    os.chdir(enter_project_name())  # change directory to project folder
    checkout_branch()
    # ide_opener()
