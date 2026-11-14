FILEPATH = "Milestones.txt"

def get_milestones(filepath=FILEPATH):
    """Read a text file and return the list of
    milestones.
    """
    with open(filepath, "r") as file_local:
        milestones_local = file_local.readlines()
    return milestones_local


def write_milestone(milestones_arg, filepath=FILEPATH):
    """ Write a list of to-do items to a text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(milestones_arg)


if __name__ == "__main__":
    print("Hello World")