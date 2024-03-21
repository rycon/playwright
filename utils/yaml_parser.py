import yaml
import os


cur_path = os.path.abspath(os.curdir)

def load_data(file_name) -> str:
    """
    This method is used to fetch data from a yaml file for use anywhere within the project.
    :param file_name: allows loading data from any yaml file.
    :return: it returns the value based on the section & variable
    """
    file_path = cur_path + file_name
    with open(file_path) as f:
        dict = yaml.safe_load(f)
        return dict

def load_test_data(file_name) -> str:
    """
    This method is used to fetch test data from a yaml file for use in tests. This is a more focused function from the
    general 'load data' function.
    :param file_name: the folder and file name from the /testdata/ folder
    :return: it returns the value based on the section & variable
    """
    file_path = cur_path + "/testdata/" + file_name
    with open(file_path) as f:
        dict = yaml.safe_load(f)
        return dict
