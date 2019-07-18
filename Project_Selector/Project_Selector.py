#! python3.7

from git import Repo
from threading import Thread
import os


class ProjectSelector():

    def __init__(project_directory="D:\\Code"):
        self.project_directory = project_directory
        self.project_dictionary = {}

    def __str__():
        return "The current Project folder is : " + self.project_directory

    def get_project_name():
        """
        Build a dictionary of all projects - consisting of {Project Name : Project Directory Path}
        :return: The Full Project Dictionary
        """
        project_names = os.listdir(self.project_directory)

        for name in project_names:
            return_dictionary[name] = os.path.join(project_directory, name)

        return return_dictionary

    def list_projects():
        """
        Print a list of all available projects
        :return: None
        """
        print("Available Projects are: ")
        for p in self.project_dictionary:
            print(p)

    def enter_project_name():
        """
        No Input params
        Get project name from user
        :return: the absolute project directory for that project
        """
        # function which will take in a project name and direct the system to
        # the associated folder
        while True:
            name_entry = raw_input(
                "Please enter project you wish to work on: ")
            try:
                return self.project_dictionary[name_entry]
            except KeyError:
                list_projects()

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
                branch = raw_input("Enter branch you want to work on: ")
                try:
                    repo_heads[branch].checkout()
                    break
                except KeyError:
                    print("Invalid Branch - input is case-sensitive")


def ide_opener():
    """
    Check if User wants an IDE open, and open it for them
    :return: None
    """
    # t = Thread(target=lambda: subprocess.call("D:\\Git\\git-bash.exe"))
    # t.start()
    loop = True
    while loop:
        ide_checker = raw_input("Do you want to open an IDE? ")
        if ide_checker == 'N':
            break
        else:
            which_ide = raw_input(
                "Do you want to open -(A)tom, (P)ycharm or (I)ntellij? or (V)sCode: ")
            if which_ide.upper() is not 'A' and not 'P' and not 'I' and not 'V':
                print("Please try again")
            elif which_ide.upper() == 'A':
                os.system("Atom .")     # Open Atom to the current Directory
                break
            elif which_ide.upper() == 'P':
                os.system("pycharm .")
                break
            elif which_ide.upper() == 'V':
                os.system("code .")
                break
    return None


# if __name__ == "__main__":
#     project_dictionary = get_project_name()
#     if len(project_dictionary) > 1:
#         list_projects()
#     else:
#         project_key = project_dictionary.keys()
#         print(f"Only Project {project_key} exists")
#     os.chdir(enter_project_name())  # change directory to project folder
#     checkout_branch()
#     ide_opener()
