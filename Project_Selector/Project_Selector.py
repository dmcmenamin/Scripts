#! python3.7

from git import Repo
from threading import Thread
import os
import subprocess

project_dictionary = {}


def get_project_name(project_directory="D:\\Code"):
    """
    :param project_directory: Project Directory
    Build a dictionary of all projects - consisting of {Project Name : Project Directory Path}
    :return: The Full Project Dictionary
    """
    return_dictionary = {}
    project_names = os.listdir(project_directory)

    for name in project_names:
        return_dictionary[name] = os.path.join(project_directory, name)

    return return_dictionary


def enter_project_name():
    """
    No Input params
    Get project name from user
    :return: the absolute project directory for that project
    """
    # function which will take in a project name and direct the system to
    # the associated folder
    while True:
        name_entry = input("Please enter project you wish to work on: ")
        try:
            return project_dictionary[name_entry]
        except KeyError:
            list_projects()


def list_projects():
    """
    Print a list of all available projects
    :return: None
    """
    print("Available Projects are: ")
    for p in project_dictionary:
        print(p)


def checkout_branch():
    """
    Search for a list of all branches for a given project
    Ask User which branch they want
    And check that branch out
    :return: None
    """
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


def ide_opener():
    """
    Open the git bash terminal
    Check if User wants an IDE open, and open it for them
    :return: None
    """
    t = Thread(target=lambda: subprocess.call("D:\\Git\\git-bash.exe"))
    t.start()
    loop = True
    while loop:
        ide_checker = input("Do you want to open an IDE? ")
        if ide_checker == 'N':
            loop = False
        else:
            which_ide = input("Do you want to open -(A)tom, (P)ycharm or (I)ntellij? ")
            if which_ide.upper() is not 'A' and not 'P' and not 'I':
                print("Please try again")
            elif which_ide.upper() == 'A':
                os.system("Atom .")     # Open Atom to the current Directory
                loop = False
            elif which_ide.upper() == 'P':
                os.system(r"C:\Program Files\JetBrains\PyCharm Community Edition 2019.1.3\bin\Pycharm64.exe "
                          r"{}".format(os.getcwd()))
                loop = False
    return None


if __name__ == "__main__":
    project_dictionary = get_project_name()
    if len(project_dictionary) > 1:
        list_projects()
    else:
        project_key = project_dictionary.keys()
        print(f"Only Project {project_key} exists")
    os.chdir(enter_project_name())  # change directory to project folder
    checkout_branch()
    ide_opener()
